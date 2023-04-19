from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("beqa", views.beqa, name="beqa"),
    path("gvantsa", views.gvantsa, name="gvantsa"),
    path("<str:name>", views.greet, name="greet")
]
