from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=15, unique=True)
    desc = models.CharField(max_length=150)