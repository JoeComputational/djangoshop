from django.contrib import admin
#Brings in our two models from models.py to use
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #brings in the category name and slug limitations from models.py
    prepopulated_fields = {'slug': ('name',)}
    #Basically prepopulates the field when the name is entered/prrepopulated
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['itemname', 'manufacturer', 'slug', 'price', 'created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug'('itemname',)}