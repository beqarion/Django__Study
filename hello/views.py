from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")
def beqa(request):
    return HttpResponse("გამარჯობა ბექა")
def gvantsa(request):
    return HttpResponse("გამარჯობა გვანცა")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })