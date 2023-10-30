from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    call_us = models.CharField(max_length=20)
    email_us = models.CharField(max_length=30) 
    subtitle = models.CharField(max_length=300)
    emails = models.TextField(max_length=100)
    phones = models.TextField(max_length=100)
    adress = models.TextField(max_length=100)
    fb_link = models.URLField(null=True,blank=True)
    tw_link = models.URLField(null=True,blank=True)
    yt_link = models.URLField(null=True,blank=True)
    android_app = models.URLField(null=True,blank=True)
    iphone_app = models.URLField(null=True,blank=True)
    app_discription = models.CharField(max_length=250,null=True,blank=True)



    def __str__(self) :
        return self.name
    

class DeliveryFee(models.Model):
    fee = models.FloatField()

    def __str__(self) -> str:
        return str(self.fee)
