from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('', list, name='list'),
    path('create/', create, name='create'),
    path('delete/<int:pk>',delete, name='delete'),
    path('update/<int:pk>',update, name='update'),
    path('patch/<int:id>',patch, name='patch'),
    
]