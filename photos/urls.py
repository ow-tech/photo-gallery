from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.my_images, name ='main'),
    path(r'search/', views.search_results, name='search_results'),
    path(r'(<int:image_id>)/', views.image_by_id, name = 'single_image'),
    path(r'(?P<location>\w+)/', views.image_location, name="locations")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)