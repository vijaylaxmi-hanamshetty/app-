from tortoise.exceptions import IntegrityError
from app.models.user_model import User
from passlib.hash import bcrypt

async def create_user(username: str, email: str, password: str) -> User:
    hashed_password = bcrypt.hash(password)
    try:
        user = await User.create(
            username=username, email=email, hashed_password=hashed_password
        )
        return user
    except IntegrityError:
        raise ValueError("User with this email or username already exists.")

async def get_user_by_email(email: str) -> User | None:
    return await User.filter(email=email).first()
