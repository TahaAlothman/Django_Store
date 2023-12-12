from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code


class Profile(models.Model):
    user = models.OneToOneField(User , related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts')
    code = models.CharField(max_length=10 ,default=generate_code)






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