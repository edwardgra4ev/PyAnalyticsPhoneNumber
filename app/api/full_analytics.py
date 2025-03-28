from fastapi import APIRouter

from app.core.models import FullAnalyticsResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/full_analytics/", response_model=FullAnalyticsResponse)
async def get_full_analytics(phone_number: str):
    return (
        Phones(phone_number)
        .is_mobile()
        .country()
        .country_code()
        .country_region()
        .national_number()
        .format_phone_number()
        .timezone()
        .result()
    )


@router.post("/full_analytics/", response_model=FullAnalyticsResponse)
async def post_full_analytics(body: PhoneModel):
    return (
        Phones(body.phone_number)
        .is_mobile()
        .country()
        .country_region()
        .country_code()
        .national_number()
        .format_phone_number()
        .timezone()
        .result()
    )
