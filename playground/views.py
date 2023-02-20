from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('''<h1> Hello <h1> <a href = ''')

def about(request):
    return HttpResponse("Hello ashutosh")

def hello(request):
    return render ()
