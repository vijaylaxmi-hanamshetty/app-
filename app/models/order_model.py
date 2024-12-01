from tortoise import fields
from tortoise.models import Model

class Order(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    total_price = fields.FloatField()
    status = fields.CharField(max_length=20, default="Pending")  # Pending, Shipped, Delivered
    created_at = fields.DatetimeField(auto_now_add=True)

    items: fields.ReverseRelation["OrderItem"]

class OrderItem(Model):
    id = fields.IntField(pk=True)
    order = fields.ForeignKeyField("models.Order", related_name="items")
    product_id = fields.IntField()
    quantity = fields.IntField()
    price = fields.FloatField()  
