from django.db import models

class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_descrption = models.TextField()
    # imange =
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    # pub_date = models.DateTimeField(auto_now_add=True, default=date.today)

    def __str__ (self):
        return self.imange_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.remove()

class Location(models.Model):
    location_name = models.CharField(max_length=30)


    def __str__ (self):
        return self.location_name

    def save_location(self):
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=30)



    def __str__ (self):
        return self.category_name

    def save_category(self):
        self.save()