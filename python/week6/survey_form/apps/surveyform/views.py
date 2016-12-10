from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render (request, 'surveyform/index.html')

def FormProcess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojoLocation'],
        "Favorite Language": request.POST['favLang'],
        "Comments": request.POST['comments']
    }
    return redirect('/showresults')

def ShowResults(request):
    print "Go to show results!"
    print request.session
    return render(request, 'surveyform/results.html')
