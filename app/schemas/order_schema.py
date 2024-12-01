from pydantic import BaseModel
from typing import List

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreateSchema(BaseModel):
    items: List[OrderItemSchema]

class OrderResponseSchema(BaseModel):
    id: int
    user_id: int
    items: List[OrderItemSchema]
    total_price: float
