from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Your database URL
        modules={"models": ["app.models.user_model", "app.models.product_model"]}  # Provide a list of strings
    )
    await Tortoise.generate_schemas()
