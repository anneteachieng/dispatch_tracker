from django.urls import path
from . import views

app_name = 'dispatches'

urlpatterns = [
    path('', views.dispatch_list, name='dispatch_list'),
]
