from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  
      modules={
    "models": [
        "app.models.user_model",
        "app.models.product_model",
        "app.models.cartitem_model",
        "app.models.order_model",
        "app.models.payment_model"
    ]
    
}
    )
    await Tortoise.generate_schemas()
