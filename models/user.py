from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    name: str
    hashed_password: str
    image: Optional[str] = None


