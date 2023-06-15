# Generated by Django 3.1.7 on 2023-06-13 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0006_remove_order_correios_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('boleto_id', models.TextField(max_length=36)),
                ('barcode', models.TextField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billings.order')),
            ],
        ),
    ]