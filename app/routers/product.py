from fastapi import APIRouter, HTTPException, Depends
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.crud.product_crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
)

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def add_product(product: ProductCreate):
    new_product = await create_product(product.dict())
    return new_product

@router.get("/", response_model=list[ProductResponse])
async def list_products():
    return await get_all_products()

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
async def edit_product(product_id: int, product: ProductUpdate):
    updated_product = await update_product(product_id, product.dict(exclude_unset=True))
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return updated_product

@router.delete("/{product_id}")
async def remove_product(product_id: int):
    success = await delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found.")
    return {"detail": "Product deleted successfully."}
