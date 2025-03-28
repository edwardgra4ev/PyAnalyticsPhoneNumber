from fastapi import APIRouter

from app.core.models import FormatPhoneNumberResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/format_phone_number/", response_model=FormatPhoneNumberResponse)
async def get_format_phone_number(phone_number: str):
    return Phones(phone_number).format_phone_number().result()


@router.post("/format_phone_number/", response_model=FormatPhoneNumberResponse)
async def post_format_phone_number(body: PhoneModel):
    return Phones(body.phone_number).format_phone_number().result()
