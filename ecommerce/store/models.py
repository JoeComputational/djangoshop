from django.db import models

class Category(models.Model):
    #This sets the maximum character count in input - also limits special characters for slugfield
    name = models.CharField(max_length=255, db_index=True)
    #Slug name is the category used in the url bar for direction - setting a max character for this - can only have one slug with the same name
    slug = models.SlugField(max_length=255, unique=True)


    class Meta:
        #Setting a plural name for django setting categorys - so correctly altered to use categories
        verbose_name_plural = 'categories'

    def __str__(self):
        #Returned data is brough up by name and not by dataset type
        return self.name
    
    
class Product(models.Model):
    #This helps associate the categories to the product as a whole - from the data table.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    #This helps record who has actually made the data that is entered into the database
    #When a user is deleted, so is their product
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    itemname = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, default='admin')
    image = models.ImageField(upload_to='images/')
    itemdescription = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)