from django.urls import path
from .import views

urlpatterns = [
        path('', views.dispatch_list, name='dispatch_list'),
        path('create/', views.create_dispatch, name='create_dispatch'),
        path('<int:pk>/', views.dispatch_detail, name='dispatch_detail'),
]

