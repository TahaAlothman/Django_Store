from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code import generate_code

ORDER_STATUS =(('Recieved','Recieved'),('Processed','Processed'),('Shipped','Shipped'),('Delivered','Delivered'))
class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_owner',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=12,choices=ORDER_STATUS,default='Recieved')
    code = models.CharField(max_length=10,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time= models.DateTimeField(null=True,blank=True)





class OrderDetail(models.Model):
    pass