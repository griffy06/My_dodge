from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserFormView.as_view(), name='login'),
    path('outpass/', include('outpass.urls')),
    path('warden/', include('warden.urls')),

]
