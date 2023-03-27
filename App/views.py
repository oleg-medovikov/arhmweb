from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from App.models import Location


def home(request):
    karta = Location.objects.all()
    return render(request, 'home.html', {"locations": karta})


def location(requests):
    pass


def add_location(requests):
    pass


def edit_location(requests):
    pass


def delete_location(requests):
    pass
