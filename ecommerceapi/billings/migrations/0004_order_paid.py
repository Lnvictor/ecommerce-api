# Generated by Django 3.1.7 on 2021-04-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0003_auto_20210405_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
