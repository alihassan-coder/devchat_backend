from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    second_name: str 
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    name: str
    image: str | None = None
