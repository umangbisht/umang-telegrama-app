from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    def __str__(self):
        return self.name
    
class BuyingOptions(models.Model):
    option_type = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.option_type

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category= models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE, null=True, blank=True)
    buying_options = models.ManyToManyField(BuyingOptions, related_name='products')  # Update this line
    def __str__(self):
        return self.name
    


    



# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()