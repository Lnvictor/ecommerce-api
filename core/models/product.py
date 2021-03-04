from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    value = models.DecimalField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name