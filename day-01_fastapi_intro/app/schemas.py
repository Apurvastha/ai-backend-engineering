from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    text: str
    email: EmailStr
    age: int

