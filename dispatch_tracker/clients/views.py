from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'staff']:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

@login_required
@staff_required
def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients/list.html", {"clients": clients})

@login_required
@staff_required
def client_create(request):
    if request.methood == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        location = request.POST['location']
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role='client')
        Client.objects.create(user=user, phone=phone, location=location)
        return redirect("clients_list")
    return render(request, 'clients/create.html')

@login_required
@staff_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/detail.html', {'client': client})

@login_required
@staff_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.user.username = request.POST['username']
        client.user.email = request.POST('email')
        if 'password' in request.POST and request.POST['password']:
            client.user.set_password(request.POST['password'])
        client.phone = request.POST['location']
        client.location = request.POST['location']
        client.user.save()
        client.save()
        return redirect('client_list')
    return render(request, 'clients,update.html', {'client': client})

@login_required
@staff_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.user.delete()
        return redirect('client_list')
    return render(request, 'clients/delete.html', {'client': client})
