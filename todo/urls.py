from turtle import update
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.deleteTask, name='delete'),
    path('update/<int:id>/', views.updateTask, name='update')

]