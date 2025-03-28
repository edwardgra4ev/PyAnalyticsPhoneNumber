from fastapi import APIRouter

from app.core.models import CountryCodeResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/country_code/", response_model=CountryCodeResponse)
async def get_country_code(phone_number: str):
    return Phones(phone_number).country_code().result()


@router.post("/country_code/", response_model=CountryCodeResponse)
async def post_country_code(body: PhoneModel):
    return Phones(body.phone_number).country_code().result()
