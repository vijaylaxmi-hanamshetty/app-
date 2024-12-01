from fastapi import APIRouter, HTTPException
from app.schemas.cart_schema import CartResponse, CartItemCreate
from app.crud.cart_crud import create_cart, get_cart, add_item_to_cart, remove_item_from_cart, clear_cart

router = APIRouter()

@router.post("/", response_model=CartResponse)
async def create_new_cart(user_id: int):
    cart = await create_cart(user_id)
    return await get_cart(user_id)

@router.get("/", response_model=CartResponse)
async def get_user_cart(user_id: int):
    cart = await get_cart(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.post("/items/", response_model=CartResponse)
async def add_item(cart_item: CartItemCreate, user_id: int):
    cart = await get_cart(user_id)
    if not cart:
        cart = await create_cart(user_id)
    await add_item_to_cart(cart.id, cart_item.product_id, cart_item.quantity)
    return await get_cart(user_id)

@router.delete("/items/{item_id}")
async def remove_item(item_id: int, user_id: int):
    cart = await get_cart(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    await remove_item_from_cart(item_id)
    return {"detail": "Item removed from cart"}

@router.delete("/")
async def clear_user_cart(user_id: int):
    cart = await get_cart(user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    await clear_cart(cart.id)
    return {"detail": "Cart cleared"}
