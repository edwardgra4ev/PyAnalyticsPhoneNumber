from fastapi import APIRouter

from app.core.models import NationalNumberResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/national_number/", response_model=NationalNumberResponse)
async def get_national_number(phone_number: str):
    return Phones(phone_number).national_number().result()


@router.post("/national_number/", response_model=NationalNumberResponse)
async def post_national_number(body: PhoneModel):
    return Phones(body.phone_number).national_number().result()
