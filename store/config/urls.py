from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import HomeView
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Store Adminstration")
admin.site.site_title = _("Store Admin")
admin.site.index_title = _("Adminstration")

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("customers.urls")),
    path("products/", include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)