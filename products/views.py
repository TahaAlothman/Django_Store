from os import name
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImage ,  Review ,Brand




def mydebug(request):
    #data = Product.objects.all()
    #data = Product.objects.filter(price__gt=90)
    #data = Product.objects.filter(price__gte=90)
    #data = Product.objects.filter(price__lte=90)
    #data = Product.objects.filter(price__range=(90,91))
    data= Product.objects.filter(name__contains='William')
   
   
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