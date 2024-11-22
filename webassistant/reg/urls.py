from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', register, name="reg"),
    path('login/', login_view, name="login"),
    path('logout/',logout_view, name="logout")
]