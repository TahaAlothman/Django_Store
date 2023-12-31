from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import ProductDetailSerializer,ProductListSerializer,BrandDetailSerializer,BrandListSerializer
from .models import Product , Brand
from .mypagination import MyPagination
from .myfilters import ProductFilter

# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()   #list
#     data = ProductSerializer(products,many=True,context={'request':request}).data   #json
#     return Response({'products':data})



# @api_view(['GET'])
# def product_detail_api(request,product_id):
#     product =  Product.objects.get(id = product_id)
#     data = ProductSerializer(product,context={'request':request}).data   #json
#     return Response({'products':data})




class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all() 
    pagination_class = MyPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['brand', 'flag']
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = ['brand', 'flag']
    ordering_fields = ['price']
    filterset_class = ProductFilter

class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class =ProductDetailSerializer
    queryset = Product.objects.all() 




class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all() 
    


class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all() 