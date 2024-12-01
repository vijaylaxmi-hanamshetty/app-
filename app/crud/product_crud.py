from app.models.product_model import Product
from tortoise.exceptions import DoesNotExist
async def create_product(name: str, description: str, price: float, stock: int):
    return await Product.create(name=name, description=description, price=price, stock=stock)

async def get_product_by_id(product_id: int):
    try:
        return await Product.get(id=product_id)
    except DoesNotExist:
        return None

async def get_all_products():
    return await Product.all()

async def update_product(product_id: int, **kwargs):
    product = await get_product_by_id(product_id)
    if product:
        await product.update_from_dict(kwargs).save()
    return product

async def delete_product(product_id: int):
    product = await get_product_by_id(product_id)
    if product:
        await product.delete()
    return product