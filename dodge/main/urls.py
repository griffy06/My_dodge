from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),

]
