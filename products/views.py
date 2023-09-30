from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product , ProductImage ,  Review





def test(request):
    data = Product.objects.all()
    return render (request, "test.html",{"data":data})



class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product


    def get_context_data(self, **kwargs) :
     context = super().get_context_data(**kwargs)
     context["product_images"] = ProductImage.objects.filter(product = self.get_object())
     context['reviews'] = Review.objects.filter(product = self.get_object())
     return context
