from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "StockFlow API is running 🚀"})

urlpatterns = [
    path('', home),   # 👈 this fixes your 404
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
]