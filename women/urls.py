from django.contrib import admin
from django.urls import path
from women.views import index
from women import views

urlpatterns = [
    path("",index),
    path("categories/<int:cat_id>",views.categories),
    path("categories/<slug:cat_slug>/",views.categories_by_slug),
    path("about/",views.about),
]
