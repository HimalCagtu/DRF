from django.urls import path
from .views import *


urlpatterns = [
    path('', listview, name="listview")
]