from django.urls import path
from .views import (
    DriverListView, DriverCreateView, DriverUpdateView, DriverDeleteView,
    DriverDetailView, my_driver_profile
)

app_name = "drivers"

urlpatterns = [
    path("", DriverListView.as_view(), name="list"),
    path("new/", DriverCreateView.as_view(), name="create"),
    path("<int:pk>/", DriverDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", DriverUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", DriverDeleteView.as_view(), name="delete"),
    path("me/", my_driver_profile, name="me"),
]
