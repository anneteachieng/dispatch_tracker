from django.urls import path
from . import views

urlpatterns = [
    path("", views.dispatch_list, name="dispatch_list"),
    path("create/", views.dispatch_create, name="dispatch_create"),
    path("<int:pk>/edit/", views.dispatch_update, name="dispatch_update"),
    path("<int:pk>/delete/", views.dispatch_delete, name="dispatch_delete"),
]
