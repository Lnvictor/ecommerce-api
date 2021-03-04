from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=150)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=3, max_digits=15)
    quantity = models.IntegerField(default=0)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
