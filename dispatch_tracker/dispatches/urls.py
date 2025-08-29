from django.urls import path
from . import views

app_name = 'dispatches'

urlpatterns = [
    path('', views.dispatch_list, name='list'),
    path('driver/my-assignments/', views.driver_assignments, name='driver-my'),
    path("client/my/", views.client_my_dispatches, name="client-my"),

]
