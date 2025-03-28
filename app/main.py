from fastapi import FastAPI

from app.api import router

app = FastAPI(
    title="PyAnalyticsPhoneNumber", description="API для аналитика номера телефона"
)

app.include_router(router, prefix="/api")
