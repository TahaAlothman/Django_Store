from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User , related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts')
    code = models.CharField(max_length=10 ,default=generate_code)


@receiver( post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )



NUMBER_TYPES = (
    ('Primary', 'Primary'),
    ('Secondary' , 'Secondary')
)
class ContactNumbers(models.Model):
    user = models.ForeignKey(User,related_name='user_phones',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=NUMBER_TYPES)
    number = models.CharField(max_length=25)





ADDRESS_TYPES = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Other','Other'),
)

class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=ADDRESS_TYPES)
    address = models.CharField(max_length=150)