from django.urls import path
from . import views
from .views import *

app_name='polls'

urlpatterns:list[path] = [

    path("", views.IndexView.as_view(), name = 'index'),
    path("<int:pk>/",views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name ='results'),
    path("<int:question_id>/vote/",vote , name = 'vote'),
]