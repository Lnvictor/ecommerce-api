"""
Products Provider Abstraction.

An provider might have one or more Product domains related to, 
and the domain product must be equal to one Provider domains collection.

Provider also might can has an own API, that must be registered
as a model field and the provider products can be loaded in 
application database calling a function that consumes provider's API

"""
from django.db import models


class GiantBombManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(name='GiantBomb')


class Provider(models.Model):
    name = models.CharField(max_length=15)
    desc = models.CharField(max_length=150)
    domains = models.ManyToOneRel(
        'core:Domain',
        field_name="domains",
        related_name="domains",
        to="domains"
    )

    cnpj = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=40)
    api_link = models.TextField(null=True)
    website_link = models.TextField(null=True)

    # managers, one by Provider API
    objects = models.Manager()
    giant_bomb = GiantBombManager()

    def __str__(self):
        return self.cnpj

    def __repr__(self):
        return self.cnpj
