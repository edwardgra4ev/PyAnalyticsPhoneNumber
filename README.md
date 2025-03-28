# PyAnalyticsPhoneNumber
API для аналитика номера телефона


# Запуск
```bash
git clone https://github.com/edwardgra4ev/PyAnalyticsPhoneNumber.git
cd PyAnalyticsPhoneNumber
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

Сборка в Docker
```bash
git clone https://github.com/edwardgra4ev/PyAnalyticsPhoneNumber.git
cd PyAnalyticsPhoneNumber
sudo docker build -t py_analytics_phone_number .
sudo docker run -d -p 8000:8000 py_analytics_phone_number   
```