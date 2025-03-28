FROM python:3.13-slim

RUN pip install uv

WORKDIR /app
COPY . .

RUN uv sync

EXPOSE 8000

# Запускаем FastAPI приложение через uvicorn
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
