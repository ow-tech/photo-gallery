from django.db import models
import datetime as date
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_descrption = models.TextField()
    image_pics = models.ImageField(upload_to = 'images/', null=False)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    pub_date =models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.image_name

    def save_image(self):
        self.save()
    

    def delete_image(self):
        self.delete()


    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_category):
        images = cls.objects.filter(category__category_name__icontains=search_category)
        return images
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id).all()
        return image
    @classmethod
    def filter_by_location(cls, location):
        image_location = cls.objects.filter(location = location).all()
        return image_location

    class Meta:
        ordering = ['pub_date']

class Location(models.Model):
    location_name = models.CharField(max_length=30)


    def __str__ (self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_category(self):
        self.delete()
    @classmethod
    def get_locations(cls):
        locations = cls.objects.filter()
        return locations


class Category(models.Model):
    category_name = models.CharField(max_length=30)



    def __str__ (self):
        return self.category_name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()