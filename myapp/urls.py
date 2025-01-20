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
    path('securityPassword/',views.SecurityPassword, name='securityPassword'),
    path('register/', views.Register,name='register'),
    path('mainMenu/', views.mainMenu,name='mainMenu'),
    path('estatus/', views.Estatus,name='estatus'),
    path('restorePassword/', views.RestorePassword,name='restorePassword'),
    path('enviar-correo/', views.enviar_correo, name='enviar_correo'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/index'), name='logout'),
]