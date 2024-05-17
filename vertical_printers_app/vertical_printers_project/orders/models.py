from datetime import date
from django.db import models
from users.models import User

ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')
    card_number = models.CharField(max_length=16, default='0000000000000000')
    expire_date = models.DateField(default=date.today)  # Store as a date
    cvv_number = models.CharField(max_length=3,  default='000')


    def __str__(self):
        return f"Order #{self.id} - {self.product_name}"