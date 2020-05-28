from rest_framework import serializers
from computerapp.models import Product, Manufacture, Category

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined',)


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = ('id', 'name',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'model', 'image', 'price', 'sold', 'category', 'manufacture')


