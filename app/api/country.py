from fastapi import APIRouter

from app.core.models import CountryResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/country/", response_model=CountryResponse)
async def get_country(phone_number: str):
    return Phones(phone_number).country().result()


@router.post("/country/", response_model=CountryResponse)
async def post_country(body: PhoneModel):
    return Phones(body.phone_number).country().result()
