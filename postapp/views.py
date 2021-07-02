from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'postapp/hello_world.html')
# Create your views here.
