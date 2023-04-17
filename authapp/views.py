from django.shortcuts import render
from django.utils import timezone
from .forms import UserRegisterForm
from .models import User

# Create your views here.
def login(request):
    return render(request, 'authapp/login.html', {})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user: User = form.save(commit=False)
            user.first_name = request.first_name
            user.last_name = request.last_name
            user.email = request.email
            user.date_joined = timezone.now()
            user.is_active = True
            user.password = request.password
            user.studio_name = request.studio_name
            user.save()
            return 
    else:
        form = UserRegisterForm()
    return render(request, 'authapp/register.html', {'form': form})

def register2(request):
    return render(request, 'authapp/register2.html', {})


