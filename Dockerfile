FROM python:3.13-slim

RUN pip install uv

WORKDIR /app
COPY . .

RUN uv sync

EXPOSE 8000

# Запускаем FastAPI приложение через uvicorn
CMD ["uv" "run" "gunicorn" "app.main:app" "--workers" "4" "--worker-class" "uvicorn.workers.UvicornWorker" "--bind" "0.0.0.0:8000"]
