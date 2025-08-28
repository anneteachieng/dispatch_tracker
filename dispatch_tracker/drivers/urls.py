from django.urls import path
from . import views

app_name = "drivers"

urlpatterns = [
    path('', views.driver_list, name='driver_list'),
    path('<int:pk>/', views.driver_detail, name='driver_detail'),
    path('create/', views.driver_create, name='driver_create'),
    path('<int:pk>/update/', views.driver_update, name='driver_update'),
    path('<int:pk>/delete/', views.driver_delete, name='driver_delete'),
]
