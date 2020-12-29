
from django.urls import path

from . import views

urlpatterns = [
    # path("", views.register, name="register"),
    path("", views.login, name="login"),
    path("register", views.register, name="register"),
]
