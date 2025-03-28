from functools import wraps
from typing import TypeVar

import phonenumbers
from phonenumbers import carrier, geocoder, region_code_for_number, timezone
from phonenumbers.phonenumberutil import number_type

T = TypeVar("T", bound="Phones")


def check_error(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if "error" in self._result:
            self._result["success"] = False
            return self
        return func(self, *args, **kwargs)

    return wrapper


class Phones(object):
    def __init__(self, phone: str):
        self.phone = phone
        self._result = {"input_phone_number": self.phone, "success": True}

        if not any(char.isdigit() or char == "+" for char in phone):
            self._result["error"] = (
                "Номер телефон может содержать только цифры и символ +"
            )

        if phone.startswith("89"):
            phone = phone.replace("8", "+7", 1)
        elif not phone.startswith("+"):
            phone = "+" + phone

        try:
            self._parsed_number = phonenumbers.parse(phone)
        except phonenumbers.phonenumberutil.NumberParseException:
            self._result["error"] = "Передан не корректный номер телефона"

    def _is_valid_number(self) -> bool:
        return phonenumbers.is_valid_number(self._parsed_number)

    @check_error
    def is_mobile(self) -> T:
        if not self._is_valid_number():
            self._result["is_mobile"] = False
        self._result["is_mobile"] = carrier._is_mobile(number_type(self._parsed_number))
        return self

    @check_error
    def country_region(self) -> T:
        self._result["country_region"] = geocoder.description_for_number(
            self._parsed_number, "ru"
        )
        return self

    @check_error
    def country(self) -> T:
        self._result["country"] = region_code_for_number(self._parsed_number)
        return self

    @check_error
    def format_phone_number(self):
        self._result["format_phone_number"] = phonenumbers.format_number(
            self._parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        return self

    @check_error
    def timezone(self) -> T:
        self._result["timezone"] = timezone.time_zones_for_number(self._parsed_number)
        return self

    @check_error
    def country_code(self) -> T:
        self._result["country_code"] = self._parsed_number.country_code
        return self

    @check_error
    def national_number(self) -> T:
        self._result["national_number"] = self._parsed_number.national_number
        return self

    def result(self):
        return self._result
