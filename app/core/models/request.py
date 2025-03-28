from pydantic import BaseModel


class PhoneModel(BaseModel):
    phone_number: str
