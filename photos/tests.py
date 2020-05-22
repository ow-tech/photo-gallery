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

        # Creating a new location and saving it
        self.new_location = Location(location_name = 'testing')
        self.new_location.save()
        # Creating a new category and saving it
        self.new_category = Category(category_name = 'testing')
        self.new_category.save()

    def test_get_images(self):
        self.expression.save_image()
        images_all = Image.all_images()
        # all_images = Image.objects.all()
        self.assertTrue(len(images_all)> 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


        

# class LocationTestClass(TestCase):

#     def setUp(self):
#         self.nairobi= Location(location_name ='nairobi',)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.nairobi,Location))

#     def test_save_method(self):
#         self.nairobi.save_location()
#         locations = Location.objects.all()
#         self.assertTrue(len(locations)> 0)


# class CategoryTestClass(TestCase):

#     def setUp(self):
#         self.city= Category(cartegory_name ='city',)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.city,Category))

#     def test_save_method(self):
#         self.city.save_image()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories)> 0)
