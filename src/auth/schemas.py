from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    name: str
    family: str
    age: int
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    family: str
    age: int
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False