from django.urls import path
from .import views

urlpatterns = [
        path('', views.dispatch_list, name='dispatch_list'),
    ]
