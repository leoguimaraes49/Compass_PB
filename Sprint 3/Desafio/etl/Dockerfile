FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy==1.23.5 pandas==1.5.3

COPY dados.csv /app/dados.csv  
COPY etl.py /app/etl.py       
CMD ["python", "etl.py"]