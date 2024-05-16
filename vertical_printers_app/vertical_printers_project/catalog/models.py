# catalog/models.py
from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to='artist_pictures/')
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
