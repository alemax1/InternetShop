from rest_framework import serializers


from .models import *


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)


class ProductsStorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsStorage
        fields = "__all__"


class ProductSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSign
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'number',
            'adress',
        ]
