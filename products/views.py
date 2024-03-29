from os import name
from pickle import TRUE
from typing import Any
from django.shortcuts import render ,redirect
from django.views.generic import ListView, DetailView
from .models import Product , ProductImage ,  Review ,Brand
from django.db.models import Q , F , Value
from django.db.models.aggregates import Min , Max , Sum , Count , Avg
from django.views.decorators.cache import cache_page

from django.http import JsonResponse
from django.template.loader import render_to_string



from .tasks import send_emails






# @cache_page(60 * 1)
def mydebug(request):
    
    #data = Product.objects.filter(price__gt=90)
    #data = Product.objects.filter(price__gte=90)
    #data = Product.objects.filter(price__lte=90)
    #data = Product.objects.filter(price__range=(90,91))
    #data = Product.objects.filter(name__contains='William')
    #data = Product.objects.filter(name__startswith='William')
    #data = Product.objects.filter(name__endswith='Hall')
    #data = Product.objects.filter(name__isnull=True)
    #data = Product.objects.filter(price__gt=90,name__startswith='William')
    
    #   Q F
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
    #data = Product.objects.order_by('price')[0]
    #data = Product.objects.earliest('price')
    #data = Product.objects.latest('price')
    #data = Product.objects.values('name','price')
    #data = Product.objects.only('name','price')
    #data = Product.objects.defer('video_url','description')
    #data=Product.objects.select_related('brand').all()  #=====> foreignkey         IMPORTANT
    #data=Product.objects.prefetch_related('brand').all()  #=====> many-to-many       IMPORTANT
    
    #'Min , Max , Sum , Count , Avg'
    
    #data=Product.objects.aggregate(Sum('price'))
    #data=Product.objects.aggregate(Avg('price'))
    #data=Product.objects.aggregate(Sum('quantitiy'))
    #data=Product.objects.aggregate(mysum=Sum('quantitiy'),myavr=Avg('price'))


    #Add new Attribute
         
    #data = Product.objects.annotate(is_new=Value(True))
    #data = Product.objects.annotate(price_with_tax=F('price')*1.25)
    data = Product.objects.all()


    send_emails.delay()

    
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
   

def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    review = request.POST['review']           #  request.POST.get('review') 
    rate = request.POST['rating']
    
    
    Review.objects.create(
        user = request.user , 
        product = product , 
        review = review , 
        rate = rate
    )
        #review
    reviews = Review.objects.filter(product=product)
    html = render_to_string('includes/product_reviews.html',{'reviews':reviews , request:request})
    return JsonResponse({'result':html})