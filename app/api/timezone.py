from fastapi import APIRouter

from app.core.models import PhoneModel, TimezoneResponse
from app.core.utils import Phones

router = APIRouter()


@router.get("/timezone/", response_model=TimezoneResponse)
async def get_timezone(phone_number: str):
    return Phones(phone_number).timezone().result()


@router.post("/timezone/", response_model=TimezoneResponse)
async def post_timezone(body: PhoneModel):
    return Phones(body.phone_number).timezone().result()
