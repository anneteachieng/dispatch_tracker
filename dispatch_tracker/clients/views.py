from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/list.html', {'clients': clients})
