from typing import List, Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    input_phone_number: str
    success: bool
    error: Optional[str] = None


class IsMobileResponse(BaseResponse):
    is_mobile: Optional[bool] = None


class CountryResponse(BaseResponse):
    country: Optional[str] = None


class FormatPhoneNumberResponse(BaseResponse):
    format_phone_number: Optional[str] = None


class TimezoneResponse(BaseResponse):
    timezone: Optional[List[str]] = None


class CountryCodeResponse(BaseResponse):
    country_code: Optional[int] = None


class NationalNumberResponse(BaseResponse):
    national_number: Optional[int] = None


class CountryRegionResponse(BaseResponse):
    country_region: Optional[str] = None


class FullAnalyticsResponse(BaseResponse):
    is_mobile: Optional[bool] = None
    country: Optional[str] = None
    format_phone_number: Optional[str] = None
    timezone: Optional[List[str]] = None
    country_code: Optional[int] = None
    national_number: Optional[int] = None
    country_region: Optional[str] = None
