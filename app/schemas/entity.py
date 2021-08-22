from typing import Optional

from pydantic import BaseModel

# Shared properties
class EntityBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on item creation
class EntityCreate(EntityBase):
    description: str


# Properties to receive on item update
class EntityUpdate(EntityBase):
    pass

"""
# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
"""