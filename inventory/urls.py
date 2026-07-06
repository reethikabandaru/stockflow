# # # from django.urls import path, include
# # # from rest_framework.routers import DefaultRouter

# # # from .views import ProductViewSet, dashboard

# # # router = DefaultRouter()
# # # router.register("products", ProductViewSet)

# # # urlpatterns = [
# # #     path("", include(router.urls)),
# # #     path("dashboard/", dashboard),
# # # ]

# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter

# # from .views import ProductViewSet, dashboard, product_page

# # router = DefaultRouter()
# # router.register("products", ProductViewSet)

# # urlpatterns = [
# #     # API routes
# #     path("", include(router.urls)),

# #     # Dashboard API
# #     path("dashboard/", dashboard),

# #     # UI page (HTML frontend)
# #     path("ui/", product_page),
# # ]



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from .views import ProductViewSet, dashboard, product_page

# router = DefaultRouter()
# router.register("products", ProductViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
#     path("dashboard/", dashboard),
#     path("ui/", product_page),   # ✅ THIS IS REQUIRED
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, dashboard, product_page

router = DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", dashboard),
    path("ui/", product_page),   # ✅ UI ROUTE
]