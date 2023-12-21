from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author' : 'rahim', 'age' : 15, 'lst' : ['python','is','best'] , 'val' : '', 'birthday' : datetime.datetime.now(),'courses' : [

        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 6000
        },
        {
            'id' : 3,
            'name' : 'algoritm',
            'fee' : 3000
        },
    ]}
    return render(request, 'home.html',d)
