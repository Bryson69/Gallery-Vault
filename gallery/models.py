from django.db import models

# Create your models here.



class Gallery(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    descripton = models.TextField(max_length=200, null=True, blank=True)
    location = models.ForeignKey('location',on_delete=models.CASCADE)
    category = models.ForeignKey('categories',on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    def update_image(self):
        self.save()

    def delete_image(self):
        self.delete()



class location(models.Model):
    location = models.TextField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()
    
    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()


class categories(models.Model):
    categories = models.TextField(max_length=200)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    def update_category(self):
        self.update()

    def delete_category(self):
        self.delete()
