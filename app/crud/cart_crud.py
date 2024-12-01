from app.models.cartitem_model import Cart, CartItem

async def create_cart(user_id: int) -> Cart:
    cart = await Cart.create(user_id=user_id)
    return cart

async def get_cart(user_id: int) -> Cart:
    return await Cart.filter(user_id=user_id).prefetch_related("items").first()

async def add_item_to_cart(cart_id: int, product_id: int, quantity: int) -> CartItem:
    item = await CartItem.create(cart_id=cart_id, product_id=product_id, quantity=quantity)
    return item

async def remove_item_from_cart(item_id: int) -> None:
    await CartItem.filter(id=item_id).delete()

async def clear_cart(cart_id: int) -> None:
    await CartItem.filter(cart_id=cart_id).delete()