
from tortoise import fields
from tortoise.models import Model
from app.models.product_model import Product  
class Cart(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="cart")
    created_at = fields.DatetimeField(auto_now_add=True)

class CartItem(Model):
    id = fields.IntField(pk=True)
    cart = fields.ForeignKeyField("models.Cart", related_name="items")
    product = fields.ForeignKeyField("models.Product", related_name="cart_items")
    quantity = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity
