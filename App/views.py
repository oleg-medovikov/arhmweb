from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from json import loads

from App.models import Location


def karta(request):
    karta = Location.objects.all()
    return render(request, 'karta.html', {"locations": karta})


def home(request):
    return render(request, 'home.html')


def location(requests):
    pass


def add_location(request):
    if request.method == "POST":
        if request.POST.get('name_node') \
                and request.POST.get('declension') \
                and request.POST.get('contact_list_id') \
                and request.POST.get('district') \
                and request.POST.get('district_id'):
            Loc = Location(
                name_node=request.POST.get('name_node'),
                declension=request.POST.get('declension'),
                contact_list_id=loads(request.POST.get('contact_list_id')),
                district=request.POST.get('district'),
                district_id=request.POST.get('district_id'),
                street=request.POST.get('street'),
                dist=request.POST.get('dist'),
                )
            Loc.node_id = Location.objects.count()
            Loc.street = True if request.POST.get('street') == 'on' else False
            Loc.dist = True if request.POST.get('dist') == 'on' else False
            Loc.save()
            messages.success(request, "Локация добавлена!")
            return HttpResponseRedirect("karta")


def edit_location(request):
    if request.method == "POST":
        print('test!')


def delete_location(requests):
    pass
