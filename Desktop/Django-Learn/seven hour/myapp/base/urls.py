
from django.urls import path
from . import views
# from views import createroom

urlpatterns = [

    path('login', views.loginpage,name='login'),
    path('signup', views.signuppage,name='signup'),
    path('logout/',views.logoutpage, name= 'logout'),
    path('',views.home, name='home'),
    path('room/<str:pk>',views.room, name= 'room'),
    path('main/',views.main, name='main'),
    path('create_room/', views.createroom, name ='createroom'),
    path('update_room/<int:pk>', views.updateroom, name ='updateroom'),
    path('delete_room/<int:pk>', views.deleteroom, name ='delete'),
    path('delete/<int:pk>', views.deletecomment, name ='deletecomment'),
    path('edit/<int:pk>', views.editcomment, name ='editcomment'),
    path('userprofile/<int:pk>', views.userprofile, name ='userprofile'),

    # path('addtopic', views.addtopic, name ='addtopic'),
    
]