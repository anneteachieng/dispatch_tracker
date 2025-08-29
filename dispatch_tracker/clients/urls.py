from django.urls import path
from .views import (
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    ClientDetailView, my_client_profile
)

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("new/", ClientCreateView.as_view(), name="create"),
    path("<int:pk>/", ClientDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", ClientUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", ClientDeleteView.as_view(), name="delete"),
    path("me/", my_client_profile, name="me"),  # client self view
]
