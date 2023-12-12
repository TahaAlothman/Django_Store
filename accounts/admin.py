from django.contrib import admin

# Register your models here.
from .models import Profile , Address , ContactNumbers



admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(ContactNumbers)