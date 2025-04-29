
import os, math, json, pandas as pd

CSV_PATH = "movies.csv"                # nome do arquivo CSV
BATCH_DIR = "batches"                  # onde ficarão ids.json …
MAX_IDS   = 100                        # 100 = limite seguro para Lambda
WAR_CODE  = "War"                      # gênero-alvo

# 1) Ler CSV 
df = pd.read_csv(
        CSV_PATH,
        sep="|",
        na_values="\\N",
        dtype=str,
        engine="python"
     )

# 2) Filmes únicos + somente gênero War
war_movies = (
    df[df["genero"].str.contains(r"(^|,)War($|,)", na=False)]
      .drop_duplicates(subset="id")
)

imdb_ids = war_movies["id"].tolist()
print(f"Total de filmes de guerra no CSV: {len(imdb_ids)}")

# 3) Gerar lotes JSON
os.makedirs(BATCH_DIR, exist_ok=True)
for i in range(math.ceil(len(imdb_ids)/MAX_IDS)):
    ids = imdb_ids[i*MAX_IDS:(i+1)*MAX_IDS]
    with open(f"{BATCH_DIR}/ids_{i+1:03d}.json", "w") as fp:
        json.dump(ids, fp)
print(f"Gerados {i+1} arquivos em '{BATCH_DIR}/'")
