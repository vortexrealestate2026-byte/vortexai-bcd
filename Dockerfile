FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "celery", "-A", "src.celery_app", "beat", "-l", "info"]
