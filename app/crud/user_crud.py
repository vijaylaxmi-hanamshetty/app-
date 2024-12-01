from tortoise.exceptions import DoesNotExist
from app.models.user_model import User
from app.core.security import hash_password, verify_password

async def create_user(username: str, email: str, password: str):
    hashed_password = hash_password(password)
    return await User.create(username=username, email=email, password_hash=hashed_password)

async def get_user_by_email(email: str):
    try:
        return await User.get(email=email)
    except DoesNotExist:
        return None

async def authenticate_user(email: str, password: str):
    user = await get_user_by_email(email)
    if user and verify_password(password, user.password_hash):
        return user
    return None
