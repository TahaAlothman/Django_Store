from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImage ,  Review ,Brand




def test(request):
    data = Product.objects.all()
    return render (request, "test.html",{"data":data})



class ProductList(ListView):
    model = Product
    paginate_by = 50



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


class BrandDetail(DetailView):
   model = Brand