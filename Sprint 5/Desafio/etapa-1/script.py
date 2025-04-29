import boto3, datetime, pathlib, os

BUCKET = os.getenv("DL_BUCKET")
SRC_DIR = pathlib.Path("/app") # volume montado

s3 = boto3.client("s3")
today = datetime.date.today()

for fname in ("movies.csv", "series.csv"):
    path = SRC_DIR / fname
    if not path.exists():
        print(f"⚠️  Arquivo {fname} não encontrado, pulei.")
        continue

    prefix = (
        f"Raw/Local/CSV/{path.stem.capitalize()}/"
        f"{today:%Y/%m/%d}/{path.name}"
    )
    print(f"⬆️  Enviando {fname} → s3://{BUCKET}/{prefix}")
    s3.upload_file(str(path), BUCKET, prefix)
    print("   ✔️  Ok")

print("🎉  Fim do upload")
