from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("sethudi", views.sethudi, name="sethudi"),
    path("semaka", views.semaka, name="semaka"),
    path("<str:name>", views.greet, name="greet")
]