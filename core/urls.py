from django.contrib import admin
from django.urls import include, path
from women.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("women/",include("women.urls")),
]
