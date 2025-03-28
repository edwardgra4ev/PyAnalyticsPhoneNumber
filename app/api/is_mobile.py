from fastapi import APIRouter

from app.core.models import IsMobileResponse, PhoneModel
from app.core.utils import Phones

router = APIRouter()


@router.get("/is_mobile/", response_model=IsMobileResponse)
async def get_is_mobile(phone_number: str):
    return Phones(phone_number).is_mobile().result()


@router.post("/is_mobile/", response_model=IsMobileResponse)
async def post_is_mobile(body: PhoneModel):
    return Phones(body.phone_number).is_mobile().result()
