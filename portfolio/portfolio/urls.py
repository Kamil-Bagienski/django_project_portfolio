from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("web/", include("web_portfolio.urls")),
    path("admin/", admin.site.urls),
]
