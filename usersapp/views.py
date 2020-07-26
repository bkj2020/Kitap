from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import OurUserRegistration
import pdb


# Create your views here.
# fanction for registration new user
def register(request):
    if request.method == "POST":
        form = OurUserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was succesfuly created')
            return redirect('log')
    else:
        form = OurUserRegistration()
    return render(request, 'registration.html', {'form': form, 'title': 'registration'})