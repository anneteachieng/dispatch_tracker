from django.shortcuts import render
from accounts.models import Client, Driver


# Demo user class
class DemoUser:
    def __init__(self, role):
        self.role = role

# Demo dashboard view
def dashboard(request):
    # 'admin', 'staff', 'driver', 'client'
    demo_role = 'admin'  
    user = DemoUser(demo_role)
    context = {}

    if user.role == 'admin':
        context['clients'] = ['Client 1', 'Client 2']  # dummy data
        context['drivers'] = ['Driver 1', 'Driver 2']
        return render(request, 'accounts/admin_dashboard.html', context)

    elif user.role == 'staff':
        context['clients'] = ['Client 1', 'Client 2']
        return render(request, 'accounts/staff_dashboard.html', context)

    elif user.role == 'driver':
        context['driver'] = {'name': 'Driver 1'}
        return render(request, 'accounts/driver_dashboard.html', context)

    elif user.role == 'client':
        context['client'] = {'name': 'Client 1'}
        return render(request, 'accounts/client_dashboard.html', context)

    else:
        return render(request, 'accounts/welcome.html')
