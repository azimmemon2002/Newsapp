
from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("sports/", views.sports, name="n_sports"),
    path("entertainment/", views.entertain, name="n_entertain"),
    path("science/", views.science, name="n_science"),
    path("business/", views.business, name="n_business"),
    path("world/", views.world, name="n_world"),
    path("national/", views.national, name="n_national"),
    path("technology/", views.technology, name="n_technology"),
    path("startup/", views.startup, name="n_startup"),
    path("hatke/", views.hatke, name="n_hatke"),
    path("politics/", views.politics, name="n_politics"),

]
