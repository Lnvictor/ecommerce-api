# Generated by Django 3.1.7 on 2021-04-07 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0005_auto_20210407_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='correios_code',
        ),
    ]
