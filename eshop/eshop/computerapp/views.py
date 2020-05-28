from django.shortcuts import render


# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from computerapp.models import Product
from computerapp.serializers import ProductListSerializer
from rest_framework.filters import OrderingFilter, SearchFilter 
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response



class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('category', 'manufacture', 'created', 'sold',)
    ordering = ('id',)
    pagination_class = LimitOffsetPagination

class ProductListByCategoryView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('description',)
    ordering_fields = ('category', 'manufacture', 'created', 'sold', 'stock', 'price',)
    def get_queryset(self):
        category = self.request.query_params.get('category', None)

        if category is not  None:
            queryset = Product.objects.filter(category=category)

        else:
            queryset = Product.objects.all()

        return queryset

