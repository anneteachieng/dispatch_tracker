from django.urls import path
from . import views

app_name = 'clients'  # allows using namespaced URLs

urlpatterns = [
    path('<int:pk>/update/', views.profile_update, name='client_update'),
    # optional success page route
    path('update-success/', views.update_success, name='client_update_success'),
]
