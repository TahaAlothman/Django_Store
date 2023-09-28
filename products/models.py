from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager




FLAG_CHOICES =(('Sale','Sale'),('New','New'),('Feature','Feature'))

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    flage = models.CharField(max_length=10,choices= FLAG_CHOICES)
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True)
    sku = models.CharField(max_length=10)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=50000)
    quantitiy = models.IntegerField()
    tags = TaggableManager()
    video_url = models.URLField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey (Product,related_name= 'product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")



class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands')
    slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str (self.product)