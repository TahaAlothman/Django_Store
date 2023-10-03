import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from products.models import Product, Brand, Review
import random
from faker import Faker


def add_brands(n):
    fake = Faker()
    images=['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image=f"brands/{images[random.randint(0,9)]}"

        )

    print(f'{n} brands was created successfully')

def add_products(n):
     fake = Faker()
     images=['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
     flags=['Sale','New','Feature']
     for x in range(n):
        Product.objects.create(
            name = fake.name(),
            image=f"product/{images[random.randint(0,9)]}" ,
            price = round(random.uniform(20.99,99.99),2)   ,
            flag = flags [random.randint(0,2)]  ,
            brand = Brand.objects.get(id =random.randint(1,50)) ,
            sku = random.randint(1000,1000000) ,
            subtitle = fake.text(max_nb_chars=200) ,
            description = fake.text(max_nb_chars=1000) ,
            quantitiy = random.randint(5,30),

        )
     print(f'{n} products was created successfully')

def add_reviews(n):
    pass

add_products(50)


