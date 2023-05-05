from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from json import loads

from App.models import Event


def events(request):
    events = Event.objects.all().order_by('-date_update')
    return render(request, 'events.html', {"events": events})



