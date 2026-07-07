from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def product_page(request):
    return render(request, "inventory/products.html")


@api_view(["GET"])
def dashboard(request):

    total_products = Product.objects.count()

    total_quantity = Product.objects.aggregate(
        total=models.Sum("quantity")
    )["total"]

    low_stock_count = Product.objects.filter(
        quantity__lte=models.F("low_stock")
    ).count()

    return Response({
        "total_products": total_products,
        "total_quantity": total_quantity,
        "low_stock_count": low_stock_count,
    })