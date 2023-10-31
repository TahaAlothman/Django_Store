from rest_framework import generics
from rest_framework.response import Response
from .serializers import CartSerializer  , OrderSerializer 
from django.contrib.auth.models import User
from products.models import Product , Brand
from .models import Cart , CartDetail , Order , OrderDetail , Coupon

class CartDetailCreateDeleteAPI(generics.GenericAPIView):
    serializer_class = CartSerializer
    
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create(user=user,status='inprogress')
        data = CartSerializer(cart).data
        return Response({'Cart':data})
    
    
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        
        cart  = Cart.objects.get(user=user,status='inprogress')
        cart_detail , created = CartDetail.objects.get_or_create(cart=cart,product=product)
        cart_detail.price = product.price
        cart_detail.quantity = quantity
        cart_detail.total = round(quantity*product.price,2)
        cart_detail.save()
        
        return Response({'message':'product was added successfully'})
        
    
    
    def delete(self,request,*args, **kwargs):
            user = User.objects.get(username=self.kwargs['username'])
            product = Product.objects.get(id=request.POST['product_id'])
            cart  = Cart.objects.get(user=user,status='inprogress')
            
            cart_detail = CartDetail.objects.get(cart=cart,product=product)
            cart_detail.delete()
            return Response({'message':'product was deleted successfully'})