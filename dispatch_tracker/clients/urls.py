from django.urls import path
from . import views
from accounts.views import profile_update

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:pk>/update/', views.client_update, name='client_update'),

]
