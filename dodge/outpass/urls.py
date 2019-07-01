from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.outpass, name='outpass'),
    path('back/<int:user_id>',views.back,name='back'),
]