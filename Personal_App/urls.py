from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin




urlpatterns = [
   # path('',views.index,name='index'),
    path('todolist_index',views.todolist_index,name='todolist_index'),

   # path('index_personal_app_add_redirect',views.index_personal_app_add_redirect,name='index_personal_app_add_redirect'),



    

    ]




