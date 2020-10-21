from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 32)
    
    class Meta:
        db_table = "categories"
    
class Product(models.Model):
    name        = models.CharField(max_length = 64)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2)
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "products"
        
class Image(models.Model):
    image_url  = models.URLField(max_length = 2048, null = True)
    product    = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "images"
        
class HtmlTag(models.Model):
    description = models.TextField()
    product     = models.OneToOneField(Product, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'html_tags'