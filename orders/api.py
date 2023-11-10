from rest_framework import generics
from rest_framework.response import Response
from .serializers import CartSerializer , OrderListSerializer , OrderDetailSerializer 
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
    

class OrderListAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def list(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        data = OrderListSerializer(queryset,many=True).data
        return Response(data)
    

class OrderDetailAPI(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer



class CreateOrderAPI(generics.GenericAPIView):
    def get(self,request,*args, **kwargs):        
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='inprogress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        
        # cart ----> order
        new_order = Order.objects.create(
            user = user , 
            coupon = cart.coupon,
            order_total_discount = cart.order_total_discount,
        )
        
        # cart_detail --> order detail 
        for object in cart_detail:
            OrderDetail.objects.create(
                order = new_order , 
                product = object.product , 
                quantity = object.quantity , 
                price = object.product.price , 
                total = object.total
                )
        cart.status = 'completed'
        cart.save()
        return Response({'message':'Your Order Was Created Succeefully'})