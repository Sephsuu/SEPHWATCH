from django.shortcuts import render, redirect
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Watch
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    latest_watchs = Watch.objects.filter(release_date__month=8, release_date__year=2024)[:3]
    for watch in latest_watchs:
        watch.price = intcomma(watch.price)

    return render(request, 'homepage/homepage.html', {'latest_watchs': latest_watchs})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if not User.objects.filter(email=email).exists():
                return messages.error(request, "E-mail address does not exist.")
            else:
                user = authenticate(email=email, password=password)

            if user is not None:
                return redirect('index')
            else:
                messages.error(request, 'Password Incorrect.')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'forms/login.html', {'form': form})

def signup(request):
    return render(request, 'forms/signup.html', {})