from django.urls import path
from .import views

urlpatterns = [
        path('', views.clients_list, name='clients_list'),
        path('new/', views.client_create, name='client_create'),
        path('<int:pk>/', views.client_detail, name='client_detail'),
        path('<int:pk>/edit/', views.client_update, name='client_update'),
        path('<int:pk>/delete/', views.client_delete, name='client_delete')
        ]
