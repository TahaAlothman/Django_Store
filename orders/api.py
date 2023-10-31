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
        pass
        
    
    
    def delete(self,request,*args, **kwargs):
       pass