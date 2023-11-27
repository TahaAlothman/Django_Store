from os import name
from pickle import TRUE
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImage ,  Review ,Brand
from django.db.models import Q , F



def mydebug(request):
    #data = Product.objects.all()
    #data = Product.objects.filter(price__gt=90)
    #data = Product.objects.filter(price__gte=90)
    #data = Product.objects.filter(price__lte=90)
    #data = Product.objects.filter(price__range=(90,91))
    #data = Product.objects.filter(name__contains='William')
    #data = Product.objects.filter(name__startswith='William')
    #data = Product.objects.filter(name__endswith='Hall')
    #data = Product.objects.filter(name__isnull=True)
    #data = Product.objects.filter(price__gt=90,name__startswith='William')
    # 
    # data = Product.objects.filter(
    #      Q(price__gt=90) |
    #      Q(name__startswith='William'))
    # data = Product.objects.filter(
    #      Q(price__gt=90) |
    #      ~Q(name__startswith='William'))
    #data = Product.objects.filter(price =F('quantitiy'))
    #data = Product.objects.order_by('price')
    #data = Product.objects.order_by('-price')
    #data = Product.objects.order_by('price','name')
    #data = Product.objects.order_by('price').reverse
    #data = Product.objects.filter(price__gt=99).order_by('price').reverse
    #data = Product.objects.order_by('price')[:10]
   # data = Product.objects.order_by('price')[0]
   # data = Product.objects.earliest('price')
    #data = Product.objects.latest('price')
    #data = Product.objects.values('name','price')
    #data = Product.objects.only('name','price')
    #data = Product.objects.defer('video_url','description')
    data=Product.objects.select_related('brand').all()  #=====> foreignkey
    return render(request,'products/debug.html',{'data':data})





def test(request):
    data = Product.objects.all()
    return render (request, "test.html",{"data":data})



class ProductList(ListView):
    model = Product
    paginate_by = 5           



class ProductDetail(DetailView):
    model = Product


    def get_context_data(self, **kwargs) :
     context = super().get_context_data(**kwargs)
     context["product_images"] = ProductImage.objects.filter(product = self.get_object())
     context['reviews'] = Review.objects.filter(product = self.get_object())
     return context



class BrandList(ListView):
   model = Brand
   paginate_by = 20


# class BrandDetail(DetailView):
#    model = Brand

class BrandDetail(ListView):
   model = Product
   template_name = 'products/brand_detail.html'
   paginate_by = 20

   def get_queryset(self):
        queryset = super(BrandDetail,self).get_queryset()
        brand = Brand.objects.get(slug = self.kwargs['slug'])
        queryset = queryset.filter(brand=brand)
        return queryset

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['brand'] = Brand.objects.get(slug = self.kwargs['slug'])
       return context