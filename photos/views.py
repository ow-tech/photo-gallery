from django.shortcuts import render, get_object_or_404
from .models import Image, Category, Location

def my_images (request):
    images = Image.all_images()
    locations = Location.get_locations()
    return render(request, "main.html",{"images":images, "locations":locations})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_category = request.GET.get("image")
        searched_images = Image.search_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'search.html',{"message":message, "images":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_by_id(request, image_id):
    images = get_object_or_404(Image, pk=image_id)
    return render(request, 'single_image.html', {"images":images})

def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'images': images})