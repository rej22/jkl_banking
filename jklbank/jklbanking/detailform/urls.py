from django.urls import path
from . import views

urlpatterns = [
    path('detailform/', views.detailform, name='detailform'),
]
