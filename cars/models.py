from django.db import models

# Create your models here.

class Car(models.Model):
    FUEL_ELECTRIC = 'E'
    FUEL_GAS = 'G'
    FUEL_DIESEL = 'D'

    FUEL_CHOICES = [
        (FUEL_ELECTRIC, 'Electric'),
        (FUEL_GAS, 'Gas'),
        (FUEL_DIESEL, 'Diesel'),
    ]
    car_make = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    year = models.IntegerField()
    registration = models.CharField(max_length=255)
    fuel = models.CharField(max_length=1, choices=FUEL_CHOICES, default=FUEL_DIESEL)
    owner = models.ForeignKey('Owner', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.car_make} {self.car_model} {self.owner}'

    class Meta:
        ordering = ['car_make', 'car_model']

class Owner(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']

