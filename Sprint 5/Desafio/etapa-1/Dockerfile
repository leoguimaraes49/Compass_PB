FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN pip install boto3

COPY script.py .

ENTRYPOINT ["python", "script.py"]
