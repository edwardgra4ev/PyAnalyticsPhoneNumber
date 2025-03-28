from fastapi import APIRouter

from .country import router as country
from .country_code import router as country_code
from .country_region import router as country_region
from .format_phone_number import router as format_phone_number
from .full_analytics import router as full_analytics
from .is_mobile import router as is_mobile
from .national_number import router as national_number
from .timezone import router as timezone

router = APIRouter()
router.include_router(country, tags=["country"])
router.include_router(country_region, tags=["country_region"])
router.include_router(country_code, tags=["country_code"])
router.include_router(national_number, tags=["national_number"])
router.include_router(timezone, tags=["timezone"])
router.include_router(is_mobile, tags=["is_mobile"])
router.include_router(format_phone_number, tags=["format_phone_number"])
router.include_router(full_analytics, tags=["full_analytics"])
