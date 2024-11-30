from app.models.product_model import Product

async def create_product(data: dict) -> Product:
    return await Product.create(**data)

async def get_all_products() -> list[Product]:
    return await Product.all()

async def get_product_by_id(product_id: int) -> Product | None:
    return await Product.filter(id=product_id).first()

async def update_product(product_id: int, data: dict) -> Product | None:
    product = await get_product_by_id(product_id)
    if product:
        await product.update_from_dict(data)
        await product.save()
        return product
    return None

async def delete_product(product_id: int) -> bool:
    product = await get_product_by_id(product_id)
    if product:
        await product.delete()
        return True
    return False
