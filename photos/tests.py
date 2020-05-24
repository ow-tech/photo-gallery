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
    def test_delete_image(self):
        self.image_test.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) == 0)
    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name = 'Kenya')
        self.location.save_location()
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)
    def test_update_location(self):
        new_location = 'Nairobi'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Nairobi')
        self.assertTrue(len(changed_location) > 0)
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

        

