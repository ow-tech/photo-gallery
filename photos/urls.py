from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.my_images, name ='main'),
    path(r'search/', views.search_results, name='search_results')
    path('image/', views.image_by_id, name = 'single_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)