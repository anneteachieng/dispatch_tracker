from django.urls import path
from . import views

app_name = 'drivers'

urlpatterns = [
    path('', views.driver_list, name='driver_list'),
    path('<int:pk>/update/', views.driver_update, name='driver_update'),
]
