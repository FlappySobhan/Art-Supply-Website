from .views import ProductsView, ProductView
from django.urls import path

urlpatterns = [
    path("", ProductsView.as_view(), name="products-list"),
    path("<pk>", ProductView.as_view(), name="product-detail"),
]