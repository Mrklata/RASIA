from django.shortcuts import render
from look.models import Image


def main_site(request):
    file = Image.objects.filter(name="main_logo")
    return render(request, 'look/main_site.html', {'file': file})


def photos(request):
    return render(request, 'look/photos.html')


def bathroom(request):
    return render(request, 'look/bathroom.html')


def kitchen(request):
    return render(request, 'look/kitchen.html')


def closet(request):
    return render(request, "look/closet.html")


def beds(request):
    return render(request, 'look/beds.html')


def other(request):
    return render(request, 'look/other.html')


def movies(request):
    return render(request, 'look/movies.html')


def from_back(request):
    return render(request, 'look/from_back.html')
# Create your views here.

