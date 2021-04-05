# Generated by Django 3.1.7 on 2021-04-04 23:53

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_provider'),
        ('billings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='products',
            field=models.ManyToManyField(default=[], to='core.Product'),
        ),
    ]