from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone







class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()





class ProductImage(models.Model):
    product = models.ForeignKey (Product,related_name= 'product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")



class Review (models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='review_user',name=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review_product')
    review = models.TextField(max_length=500)
    created_at = models.DateField(default=timezone.now)
    rate = models.IntegerField()