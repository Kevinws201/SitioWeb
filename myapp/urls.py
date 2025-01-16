from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home),
    path('about/',views.about, name='about'),
    path('index/', views.index, name='home'),
    path('inicio/',views.Home,name='inicio'),
    path('login/', CustomLoginView.as_view(),name='login'),
    path('SecurityPassword/',views.Password, name='password'),
    path('new/', views.newAccount,name='new'),
    path('mainMenu/', views.mainMenu,name='mainMenu'),
    path('estatus/', views.Estatus,name='estatus'),
    path('carrusel/', views.carrusel,name='carrusel'),
    path('enviar-correo/', views.enviar_correo, name='enviar_correo'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/index'), name='logout'),
]