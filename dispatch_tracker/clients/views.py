from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from accounts.forms import UserUpdateForm

def profile_update(request, pk):
    """
    Allows updating a client's profile.
    """
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('clients:client_update_success')
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'clients/profile_form.html', {'form': form})

def update_success(request):
    return render(request, 'clients/update_success.html')
