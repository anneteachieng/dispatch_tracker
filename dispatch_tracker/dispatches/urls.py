from django.urls import path
from .import views

urlpatterns = [
        path('', views.dispatch_list, name='dispatch_list'),
        path('new/', views.dispatch_create, name='dispatch_create'),
        path('<int:pk>/', views.dispatch_detail, name='dispatch_detail'),
        path('<int:pk>/edit/', views.dispatch_update, name='dispatch_update'),
]

