from django.db import models
from users.models import User
from printers.models import Printers



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.printer.name

    def add_amount(self):
        amount = self.printer.price * self.quantity
        return amount

    def save(self, *args, **kwargs):
        self.total_price = self.add_amount()
        return super(CartItem, self).save(*args, **kwargs)

