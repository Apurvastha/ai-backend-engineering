from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    age:int = Field(gt=0, lt=120)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price:float = Field(gt=0)
    stock:int = Field(gt=0)