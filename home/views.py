from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    return render(request, 'home/welcome.html')

def register(request):

    if request.user.is_authenticated:
        return redirect('', username=request.user.username)

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('signup')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})