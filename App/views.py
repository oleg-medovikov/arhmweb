from django.shortcuts import render
from App.models import Location


def home(request):
    karta = Location.objects.all()
    return render(request, 'home.html', {"locations": karta})
