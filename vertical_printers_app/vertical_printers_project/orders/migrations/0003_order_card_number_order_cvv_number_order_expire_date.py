# Generated by Django 5.0.6 on 2024-05-17 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(default='0000000000000000', max_length=16),
        ),
        migrations.AddField(
            model_name='order',
            name='cvv_number',
            field=models.CharField(default='000', max_length=3),
        ),
        migrations.AddField(
            model_name='order',
            name='expire_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
