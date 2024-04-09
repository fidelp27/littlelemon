from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return self.name
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="No title")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(max_length=500, default="No description available")
    image = models.ImageField(upload_to='menu_images', default='{%static "assets/menu_images"%}')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)      

    def __str__(self):
        return self.title + " " + self.price + " " + self.description + " " + self.inventory

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="No name")
    no_of_guest = models.IntegerField(default=0)
    booking_date = models.DateField(default="2021-01-01") 

    def __str__(self):
        return self.name + " " + self.booking_date + " " + self.no_of_guest + " " + self.id