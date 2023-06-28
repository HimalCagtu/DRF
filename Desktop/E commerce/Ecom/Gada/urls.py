from django.urls import path
from .views import signup_form, loginpage,homepage,logout


urlpatterns = [

    path('signup', signup_form, name = 'signup'),
    path('login', loginpage, name = 'login'),
    path('',homepage, name = 'home'),
    path('logout',logout, name = 'logout'),
]