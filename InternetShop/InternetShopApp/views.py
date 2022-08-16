from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics, viewsets

from .serializers import *
from .permissions import IsAdminOrReadOnly
from .filters import *


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('title', 'category__name')
    filter_fields = ('category',)
    ordering_fields = ('price',)
    filterset_class = ProductsFilter


class StorageViewSet(viewsets.ModelViewSet):
    queryset = ProductsStorage.objects.all()
    serializer_class = ProductsStorageSerializer
    permission_classes = (IsAdminUser,)


class ProductSignViewSet(viewsets.ModelViewSet):
    queryset = ProductSign.objects.all()
    serializer_class = ProductSignSerializer
    permission_classes = (IsAdminUser,)


class OrderCreateAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
