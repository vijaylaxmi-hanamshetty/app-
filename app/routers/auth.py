from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from app.crud.user_crud import create_user, get_user_by_email
from app.core.security import verify_password

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    created_user = await create_user(user.username, user.email, user.password)
    return created_user

@router.post("/login")
async def login_user(email: str, password: str):
    user = await get_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"message": "Login successful"}
