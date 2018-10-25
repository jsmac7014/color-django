from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import Color
from django.utils import timezone
from .forms import ColorForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            raw_password = form.data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'cooler/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = form.data['username']
        password = form.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return 'invalid login'

def logout_view(request):
    logout(request)
def color_list(request):
    colors = Color.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cooler/color_main.html', {'colors': colors})

def color_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    # color = get_object_or_404(Color)
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if(form.is_valid()):
            color = Color()
            color.title = form.data['title']
            color.colorCode = form.data['colorCode']
            color.author = request.user
            color.published_date = timezone.now()
            color.save()
            return HttpResponseRedirect('/')
    else:
        form = ColorForm()
    return render(request, 'cooler/color_make.html', {'form': form})


