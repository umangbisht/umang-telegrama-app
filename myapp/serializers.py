from rest_framework import serializers
from .models import Product, BuyingOptions, Category

class BuyingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingOptions
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    buying_options = BuyingOptionSerializer(many=True, read_only=True)
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"





# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'