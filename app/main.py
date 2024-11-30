from fastapi import FastAPI
from app.database import init_db
from app.routers import auth,product

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(product.router, prefix="/products", tags=["Products"])
@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API"}
