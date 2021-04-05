# Generated by Django 3.1.7 on 2021-04-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_product_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('correios_code', models.TextField()),
                ('delivery_status', models.BooleanField()),
                ('products', models.ManyToManyField(to='core.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('products', models.ManyToManyField(to='core.Product')),
            ],
        ),
    ]