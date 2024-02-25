from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('about/',views.about),
    path('index/', views.index),
    path('inicio/',views.Home),
    path('login/', views.Login),
    path('password/',views.Password),
    path('new/', views.newAccount),
    path('mainMenu/', views.mainMenu),
]