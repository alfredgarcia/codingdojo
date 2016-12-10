from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    context = {
        'view_all': False,
        'no_ninjas': True,
    }
    return render(request, 'disappearingninjas/index.html', context)

def all(request):
    context = {
        'view_all': True,
        'no_ninjas': False,
    }
    return render(request, 'disappearingninjas/index.html', context)

def ninja(request, color):
    if color == 'blue' or color == 'red' or color == 'purple' or color == 'orange':
        context = {
            'view_all' : False,
            'no_ninjas': False,
            'color': color,
        }
    else:
        context = {
            'view_all': False,
            'no_ninjas': False,
            'megan': True,
        }
    return render(request, 'disappearingninjas/index.html', context)
