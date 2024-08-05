from django.shortcuts import render
from .models import Product, BuyingOptions, Category
from .serializers import ProductSerializer, BuyingOptionSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class BuyingOptionsViewSet(viewsets.ModelViewSet):
    queryset = BuyingOptions.objects.all()
    serializer_class = BuyingOptionSerializer

    @action(detail=True, methods=['get'], url_path='options-by-product')
    def options_by_product(self, request, pk=None):
        print(f"Received request for product ID: {pk}")
        if pk is not None:
            options = BuyingOptions.objects.filter(product_id=pk)
            print(f"Options queryset: {options}")
            serializer = BuyingOptionSerializer(options, many=True)
            print(f"Serialized data: {serializer.data}")
            return Response(serializer.data)
        return Response({"error": "Product ID not provided"}, status=400)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CartItemViewSet(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer