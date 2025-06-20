from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    birthdate: date
    city: str
    postal_code: str
    password: str

class UserOut(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    city: str
    postal_code: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: str
    password: str