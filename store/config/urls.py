from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("customers.urls")),
    path("products/", include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)