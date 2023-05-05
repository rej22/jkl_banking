from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('detailform', views.detailform, name='detailform'),
    path('logout', views.logout, name= 'logout'),
]