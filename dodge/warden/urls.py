from django.urls import path
from . import views

urlpatterns = [
    path('', views.warden, name='warden'),
    path('<int:pk>/', views.index, name='index'),
]