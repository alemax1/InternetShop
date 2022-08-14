from django_filters.rest_framework import FilterSet
from .models import Products


class ProductsFilter(FilterSet):
    class Meta:
        model = Products
        fields = {
            'category': ['exact'],
            'is_hit': ['exact'],
            'price': ['gt', 'lt']
        }
