from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    pass

class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='/products',blank=True,null=True)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING="pending"
        CONFIRMED="confirmed"
        CANCELLED="cnacelled"

    order_id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(
        max_length=10, choices=StatusChoices.choices,
        default=StatusChoices.PENDING
        )
    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    