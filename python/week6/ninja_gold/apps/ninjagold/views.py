from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['comments']
    except:
        request.session['comments'] = [{'style': 'white', 'comment': 'Welcome to ninja gold'}]
    return render(request, 'ninjagold/index.html')

def generate_gold(request):
    mylam = lambda x,y:random.randrange(x,y)
    data = {'cave':mylam(5,10), 'farm':mylam(10,20), 'casino':mylam(-50,50), 'house':mylam(2,5)}
    try:
        request.POST['building']
        request.session['gold'] += data[request.POST['building']]
        if data[request.POST['building']] > 0:
            style = 'gained'
        else:
            style = 'lost'
        request.session['comments'].append({'style':style, 'comment':"You entered the {} and {} {} gold.".format(request.POST['building'], style, data[request.POST['building']])})
    except:
        print 'fail'
    return redirect('/')

def reset(request):
    request.session.pop('gold')
    request.session.pop('comments')
    return redirect('/')
