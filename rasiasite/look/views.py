from django.shortcuts import render
from .form import FileForm
from .models import File


def main_site(request):
    file = File.objects.all()[0]
    return render(request, 'look/main_site.html', {"file": file})


def photos(request):
    return render(request, 'look/photos.html')


def photo_upload(request):
    form = FileForm()
    return render(request, 'look/photos_upload.html', {
        'form': form
    })


def bathroom(request):
    return render(request, 'look/bathroom.html')


def kitchen(request):
    return render(request, 'look/kitchen.html', {"title": "kitchen"})


def closet(request):
    return render(request, "look/closet.html", {"title": "closet"})


def beds(request):
    return render(request, 'look/beds.html')


def other(request):
    return render(request, 'look/other.html')


def movies(request):
    return render(request, 'look/movies.html')


def from_back(request):
    return render(request, 'look/from_back.html')
# Create your views here.

