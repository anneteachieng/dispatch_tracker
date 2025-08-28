from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispatch_list, name='dispatch_list'),
    path('create/', views.dispatch_create, name='dispatch_create'),
]
