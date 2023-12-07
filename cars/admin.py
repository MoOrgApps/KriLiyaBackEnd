from django.contrib import admin
from cars import models

# Register your models here.

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'car_model',  'year', 'registration','fuel','owner']
    #list_editable = ['fuel']
    list_per_page = 10
    ordering = ['car_make', 'car_model']
    search_fields = ['car_make__istartswith']

@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name']    