from django.contrib import admin
from django.urls import reverse
from genericRentalApp import models
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count

# Register your models here.


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.register(models.RentedItem)
class RentedItemAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id',  'content_object']
    #list_editable = ['content_object']
    list_per_page = 10
    
@admin.register(models.Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['customer','rentedItem','start_date','end_date']

   