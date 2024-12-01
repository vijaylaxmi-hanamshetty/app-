from fastapi import APIRouter, HTTPException
from app.schemas.order_schema import OrderCreateSchema, OrderResponseSchema
from app.crud.order_crud import create_order, get_user_orders, get_order_details
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderResponseSchema)
async def place_order(order: OrderCreateSchema, user_id: int):
    """
    Place an order for the given user.
    """
    try:
        new_order = await create_order(user_id, order.items)
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[OrderResponseSchema])
async def get_orders(user_id: int):
    """
    Retrieve all orders for a given user.
    """
    return await get_user_orders(user_id)

@router.get("/{order_id}", response_model=OrderResponseSchema)
async def get_order(order_id: int, user_id: int):
    """
    Retrieve details of a specific order for the given user.
    """
    order = await get_order_details(order_id, user_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
