from tortoise.models import Model
from tortoise import fields

class Cart(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    items = fields.ReverseRelation["CartItem"]

class CartItem(Model):
    id = fields.IntField(pk=True)
    cart = fields.ForeignKeyField("models.Cart", related_name="items")
    product_id = fields.IntField()
    quantity = fields.IntField()
    total_price = fields.FloatField(default=0.0)
def __str__(self):
        return f"CartItem(Cart={self.cart.id}, Product={self.product.id}, Quantity={self.quantity})"
