from django.contrib import admin
from .models import Organization, Product

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "quantity",
        "selling_price",
        "organization",
    )

    search_fields = ("name", "sku")