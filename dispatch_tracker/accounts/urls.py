from django.urls import path
from .views import (
    login_view,
    logout_view,
    dashboard,
    edit_client,
    edit_driver,
)

urlpatterns = [
    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Profile editing
    path('client/edit/<int:pk>/', edit_client, name='edit_client'),
    path('client/edit/', edit_client, name='edit_own_client'),  # edit self
    path('driver/edit/<int:pk>/', edit_driver, name='edit_driver'),
    path('driver/edit/', edit_driver, name='edit_own_driver'),  # edit self
]
