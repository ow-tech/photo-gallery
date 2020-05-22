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
