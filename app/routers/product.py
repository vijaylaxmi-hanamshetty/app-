from fastapi import APIRouter, HTTPException, Depends
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductOut
from app.crud.product_crud import create_product, get_product_by_id, get_all_products, update_product, delete_product

router = APIRouter()

@router.post("/", response_model=ProductOut)
async def create_new_product(product: ProductCreate):
    return await create_product(**product.dict())

@router.get("/{product_id}", response_model=ProductOut)
async def read_product(product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=list[ProductOut])
async def read_all_products():
    return await get_all_products()

@router.put("/{product_id}", response_model=ProductOut)
async def update_existing_product(product_id: int, product: ProductUpdate):
    updated_product = await update_product(product_id, **product.dict(exclude_unset=True))
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}")
async def delete_existing_product(product_id: int):
    product = await delete_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
