from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.crud.user_crud import create_user, authenticate_user
from app.utils.helpers import create_access_token
router=APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    existing_user = await create_user(user.username, user.email, user.password)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return existing_user

@router.post("/login")
async def login(user: UserLogin):
    authenticated_user = await authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": authenticated_user.email})
    return {"access_token": token, "token_type": "bearer"}
