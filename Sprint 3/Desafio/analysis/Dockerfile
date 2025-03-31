FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy==1.23.5 pandas==1.5.3 matplotlib==3.7.1 seaborn==0.12.2

COPY job.py /app/job.py  
CMD ["python", "job.py"]