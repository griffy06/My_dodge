from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserFormView.as_view(), name='register'),
]