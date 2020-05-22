from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.expression= Image(image_name ='expression', image_descrption ='This is an image that shows my expression',)

    def test_instance(self):
        self.assertTrue(isinstance(self.expression,Image))

    def test_save_method(self):
        self.expression.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)
class LocationTestClass(TestCase):

    def setUp(self):
        self.nairobi= Location(location_name ='nairobi',)

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)
class CategoryTestClass(TestCase):

    def setUp(self):
        self.city= Category(cartegory_name ='city',)

    def test_instance(self):
        self.assertTrue(isinstance(self.city,Category))

    def test_save_method(self):
        self.city.save_image()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)
