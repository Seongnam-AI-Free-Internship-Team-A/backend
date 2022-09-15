from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_img_url, name='images'),
    path('<Id>', views.delete_images, name='delete_images'),
    path('list/history', views.get_history, name='get_history')#나중에 알맞은 이름으로 수정 
   
]
