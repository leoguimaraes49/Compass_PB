import os
import json
import time
import boto3
import requests
from datetime import datetime, timezone

# ─────────────────────────────────────────────────────────────────────────────
# Configurações
# ─────────────────────────────────────────────────────────────────────────────
TMDB_API    = "https://api.themoviedb.org/3"
TMDB_KEY    = os.environ["TMDB_API_KEY"] 
S3_BUCKET   = os.environ["DL_BUCKET"]     
S3_PREFIX   = "Raw/TMDB/JSON/Movies"      # Estrutura de pastas
MAX_PER_FILE = 100                        # Garante arquivos <10 MB

s3 = boto3.client("s3")

# ─────────────────────────────────────────────────────────────────────────────
# Acesso à API TMDB
# ─────────────────────────────────────────────────────────────────────────────
def tmdb_find(imdb_id: str) -> str | None:
    """Converte IMDb ID para TMDB ID"""
    url = f"{TMDB_API}/find/{imdb_id}"
    try:
        res = requests.get(
            url,
            params={"api_key": TMDB_KEY, "external_source": "imdb_id"},
            timeout=10
        ).json()
        return res.get("movie_results", [{}])[0].get("id")
    except Exception as e:
        print(f"[ERRO] Busca TMDB: {imdb_id} - {str(e)}")
        return None

def tmdb_movie(tmdb_id: str) -> dict:
    """Busca detalhes completos do filme"""
    url = f"{TMDB_API}/movie/{tmdb_id}"
    try:
        return requests.get(
            url,
            params={"api_key": TMDB_KEY, "append_to_response": "credits,external_ids"},
            timeout=10
        ).json()
    except Exception as e:
        print(f"[ERRO] Detalhes TMDB: {tmdb_id} - {str(e)}")
        return {}

# ─────────────────────────────────────────────────────────────────────────────
# Handler Principal
# ─────────────────────────────────────────────────────────────────────────────
def lambda_handler(event, _context):
    # 1) Normalização da entrada
    imdb_ids = event.get("imdb_ids") if isinstance(event, dict) else event
    if not isinstance(imdb_ids, list):
        return {"status": "erro", "detail": "Formato de entrada inválido"}

    payload = []
    
    # 2) Processamento dos IDs
    for imdb_id in imdb_ids:
        try:
            # 2.1) Busca dados básicos
            tmdb_id = tmdb_find(imdb_id)
            if not tmdb_id:
                continue
            
            # 2.2) Busca detalhes completos
            movie = tmdb_movie(tmdb_id)
            if not movie.get("id"):
                continue

            # 2.3) Monta registro com dados complementares
            payload.append({
                "imdb_id": imdb_id,
                "tmdb_id": tmdb_id,
                "overview": movie.get("overview", ""),
                "budget": movie.get("budget"),
                "revenue": movie.get("revenue"),
                "poster_path": movie.get("poster_path"),
                "production_companies": [
                    co["name"] for co in movie.get("production_companies", [])
                ],
                "cast": [
                    {"name": c["name"], "character": c.get("character", "")}
                    for c in movie.get("credits", {}).get("cast", [])[:5]  # Top 5
                ],
                "directors": [
                    c["name"] for c in movie.get("credits", {}).get("crew", [])
                    if c.get("job") == "Director"
                ],
                "created_at": datetime.now(timezone.utc).isoformat()
            })
            
            time.sleep(0.35)  # Controle de rate limit (3 req/seg)
            
        except Exception as e:
            print(f"[ERRO CRÍTICO] {imdb_id} - {str(e)}")

    # 3) Geração dos arquivos
    if not payload:
        return {"batches": 0, "detail": "Nenhum dado complementar encontrado"}

    batches = [
        payload[i:i + MAX_PER_FILE] 
        for i in range(0, len(payload), MAX_PER_FILE)
    ]

    # 4) Upload para S3
    for batch_num, batch in enumerate(batches):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        s3_key = (
            f"{S3_PREFIX}/"
            f"{datetime.now(timezone.utc):%Y/%m/%d}/"
            f"batch_{timestamp}_{batch_num:04d}.json"
        )
        
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=json.dumps(batch, ensure_ascii=False).encode("utf-8"),
            ContentType="application/json"
        )
        print(f"[SUCESSO] {len(batch)} registros em {s3_key}")

    return {"batches": len(batches), "total_records": len(payload)}