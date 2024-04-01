from django.db import models

# Create your models here.
class Menu(models.Model):
    def __init__(self, id, title, price, description, image, inventory):
        self.id = id
        self.title = title
        self.price = price
        self.inventory = inventory
        self.description = description
        self.image = image

    def __str__(self):
        return self.name + " " + self.price + " " + self.description + " " + self.inventory

class Reservation(models.Model):
    def __init__(self, id, name, no_of_guest, booking_date):
        self.id = id
        self.name = name
        self.no_of_guest = no_of_guest
        self.booking_date = booking_date
        

    def __str__(self):
        return self.name + " " + self.booking_date + " " + self.no_of_guest + " " + self.id