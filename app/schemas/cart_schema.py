from pydantic import BaseModel

class CartItemBase(BaseModel):
    product_id: int
    quantity: int
    total_price: float

    class Config:
        orm_mode = True 
class CartBase(BaseModel):
    items: list[CartItemBase]

    class Config:
        orm_mode = True
