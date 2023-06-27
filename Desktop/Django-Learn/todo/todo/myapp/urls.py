from django.urls import path
from . import views
from .views import *




urlpatterns = [

    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginpage,name="login"),
    path('logout',views.logoutpage,name="logout"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('edit/<int:pk>',views.edittask,name="edit"),
    path('complete/<int:pk>',views.completed,name="complete"),
    path('remove/<int:pk>',views.removecompleted,name="remove"),
]