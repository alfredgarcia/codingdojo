from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'randomwordgenerator/index.html')

def randomwordgen(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    my_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    for times in range (0, 14):
        word = word + str(random.choice(my_letters))
    words = {
        'random_word': word
    }
    return render(request, 'randomwordgenerator/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
