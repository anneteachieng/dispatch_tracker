from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('<int:pk>/update/', views.profile_update, name='client_update'),
    # optional success page route
    path('update-success/', views.update_success, name='client_update_success'),
]
