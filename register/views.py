# register/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login or home page after successful registration
            return redirect('login')  # Replace 'login' with your login URL
    else:
        form = UserCreationForm()

    return render(request, 'register/register.html', {'form': form})
