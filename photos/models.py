from django.db import models

class Image(models.Model):
    imange_name = models.CharField(max_length=20)
    image_Descrption = models.TextField()
    # imange =
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    def __str__ (self):
        return self.imange_name

class Location(models.Model):
    location_name = models.CharField(max_length=30)


    def __str__ (self):
        return self.imange_name
class Category(models.Model):
    category_name = models.CharField(max_length=30)



    def __str__ (self):
        return self.imange_name