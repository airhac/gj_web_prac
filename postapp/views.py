from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    if request.method == 'POST':
        return render(request, 'postapp/hello_world.html', context={'text':'POST METHOD!'})
    else:
        return render(request, 'postapp/hello_world.html', context={'text':'GET METHOD!'})
# Create your views here.
