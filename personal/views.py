from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'personal/home.html')
    #return HttpResponse('<h1>Hi Sunil</h1>')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Please email me to contact me','sunylkumar18@gmail.com']})
