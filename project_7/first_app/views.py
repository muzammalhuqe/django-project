from django.shortcuts import render
from first_app.forms import StudentModel
# Create your views here

def home(request):
    std = StudentModel
    return render(request, 'home.html', {"form" : std})
