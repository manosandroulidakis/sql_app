from typing import Union

from pydantic import BaseModel

# users
class UserBase(BaseModel):
    email: str
    name: str
    surname: str
    physical_address: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True



# cds
class CDBase(BaseModel):
    title: str
    duration: float
    year_of_release: int
    price: float


class CDCreate(CDBase):
    pass


class CD(CDBase):
    id: int

    class Config:
        orm_mode = True
        
        
# vinyls   
class VINYLBase(BaseModel):
    pass
    # title: str
    # description: Union[str, None] = None


class VINYLCreate(VINYLBase):
    pass


class VINYL(VINYLBase):
    # id: int
    # owner_id: int

    class Config:
        orm_mode = True