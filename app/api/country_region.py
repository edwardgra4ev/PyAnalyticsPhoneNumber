from fastapi import APIRouter

from app.core.models import CountryRegionResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/country_region/", response_model=CountryRegionResponse)
async def get_country_region(phone_number: str):
    return Phones(phone_number).country_region().result()


@router.post("/country_region/", response_model=CountryRegionResponse)
async def post_country_region(body: PhoneModel):
    return Phones(body.phone_number).country_region().result()
