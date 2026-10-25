
from pydantic import BaseModel, EmailStr


class Application(BaseModel):
    name: str
    email: EmailStr
    description: str

class ConfirmApplication(BaseModel):
    recipient: EmailStr

class ApplicationUrl(BaseModel):
    token: str
