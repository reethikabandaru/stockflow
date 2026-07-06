from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    organization = models.ForeignKey(
    Organization,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    name = models.CharField(max_length=100)

    sku = models.CharField(max_length=50)

    description = models.TextField(blank=True)

    quantity = models.IntegerField(default=0)

    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    low_stock = models.IntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name