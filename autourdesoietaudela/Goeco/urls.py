from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("composteur_page/", views.composteur_page, name="composteurs"),
]