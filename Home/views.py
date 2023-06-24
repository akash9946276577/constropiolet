from django.shortcuts import render
from django.http import HttpResponse
from .models import Materials


# Create your views here.

def home(request):
    materials = Materials.objects.all
    return render(request,'materials.html', {'materials': materials})

def about(request):
    return HttpResponse("<h1> about </h1>")


def contact(request):
    return HttpResponse("<h1> contact us on +91 9946276577")
