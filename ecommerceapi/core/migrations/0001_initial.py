# Generated by Django 3.1.7 on 2021-04-04 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('desc', models.CharField(max_length=150)),
                ('value', models.DecimalField(decimal_places=3, max_digits=15)),
                ('quantity', models.IntegerField(default=0)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.domain')),
            ],
        ),
    ]
