# Create your views here.
from django.shortcuts import render, redirect
from models import Course

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    course_to_delete = Course.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'courses_app/confirm_delete.html', { 'course' : course_to_delete })

    # Otherwise it's a post and let's delete the course...
    course_to_delete.delete()
    return redirect('/')
