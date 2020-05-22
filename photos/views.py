from django.shortcuts import render
from .models import Image

def my_images (request):
    images = Image.all_images()
    return render(request, "main.html",{"images":images})
