from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def client_list(request):
    return render(request, 'clients/list.html', {'clients': []})
