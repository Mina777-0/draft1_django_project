from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from .models import station, Trip, Passenger

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

class AddPassenger(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = "__all__"

class Register(UserCreationForm):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = {"first_name", "last_name", "username", "email", "password1", "password2"}


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('index')
        else:
            return render(request, "app/login.html", {'message': "Invalid account"})
    return render(request, "app/login.html")


@login_required(login_url='log_in')
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('log_in'))
    if request.method == "POST":
        form = AddPassenger(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddPassenger()
    return render(request, "app/index.html",{'stations': station.objects.all(), 'trips': Trip.objects.all(), 'form': AddPassenger()})


@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return render(request, "app/login.html")


def signup(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/signup.html',{'message': "you've been added"})
    else:
        form = Register()
    return render(request, "app/signup.html", {'form': form})


@login_required(login_url='log_in')
def passengers(request, trip_id):
    passenger = Trip.objects.get(id = trip_id)
    return render(request, "app/passengers.html", {'attendees': passenger.passenger.all()})

def password_success(request):
    return render(request, "app/password_success.html")