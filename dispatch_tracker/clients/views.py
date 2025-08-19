from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm

@login_required
def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients/list.html", {"clients": clients})

@login_required
def client_create(request):
    if request.methood == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clients_list")

        else:
            form = ClientForm()
        return render(request, "clients/form.html", {"form": form})
