from django.shortcuts import render
from .models import Image

def my_images (request):
    images = Image.all_images()
    return render(request, "main.html",{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_category = request.GET.get("image")
        searched_images = Image.search_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_by_id(request):
    image = Image.get_image_by_id()
    return render(request, 'single_image.html', {"image":image})