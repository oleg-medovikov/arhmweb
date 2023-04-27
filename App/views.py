from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from json import loads

from App.models import Location


def karta(request):
    karta = Location.objects.all().order_by('-date_update')
    return render(request, 'karta.html', {"locations": karta})


def home(request):
    return render(request, 'home.html')


def location(request, node_id):
    location = Location.objects.get(node_id=node_id)
    if location is not None:
        return render(request, "edit_location.html", {'location': location})


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
            Loc.street = True if Loc.street == 'True' else False
            Loc.dist = True if Loc.dist == 'True' else False
            Loc.save()
            messages.success(request, "Локация добавлена!")
            return HttpResponseRedirect("karta")


def edit_location(request):
    if request.method == "POST":
        location = Location.objects.get(node_id=request.POST.get('node_id'))
        if location is not None:
            location.name_node = request.POST.get('name_node')
            location.declension = request.POST.get('declension')

            list_ = loads(request.POST.get('contact_list_id'))
            location.contact_list_id = list_

            location.district = request.POST.get('district')
            location.district_id = request.POST.get('district_id')
            location.street = request.POST.get('street')
            location.dist = request.POST.get('dist')
            location.save()
            messages.success(request, "Локация обновлена!")
            return HttpResponseRedirect("karta")


def delete_location(requests):
    pass
