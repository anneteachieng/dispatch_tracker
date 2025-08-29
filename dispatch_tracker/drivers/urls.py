from django.urls import path
from . import views
from accounts.views import profile_update


app_name = 'drivers'

urlpatterns = [
    path('', views.driver_list, name='driver_list'),
    path('<int:pk>/update/', views.driver_update, name='driver_update'),
    path('<int:pk>/delete/', views.driver_update, name='driver_delete'),
    path('<int:pk>/create/', views.driver_create, name='driver_create'),
]
