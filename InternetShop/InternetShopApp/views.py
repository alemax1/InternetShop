from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics

from .serializers import *
from .permissions import IsAdminOrReadOnly
from .filters import *


class ProductsAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('title', 'category__name')
    filter_fields = ('category',)
    ordering_fields = ('price',)
    filterset_class = ProductsFilter


class ProductsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ProductsAPIRemove(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class StorageAPIList(generics.ListCreateAPIView):
    queryset = ProductsStorage.objects.all()
    serializer_class = ProductsStorageSerializer
    permission_classes = (IsAdminUser,)


class StorageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductsStorage.objects.all()
    serializer_class = ProductsStorageSerializer
    permission_classes = (IsAdminUser,)


class StorageAPIRemove(generics.RetrieveDestroyAPIView):
    queryset = ProductsStorage.objects.all()
    serializer_class = ProductsStorageSerializer
    permission_classes = (IsAdminUser,)


class ProductSignAPIList(generics.ListCreateAPIView):
    queryset = ProductSign.objects.all()
    serializer_class = ProductSignSerializer
    permission_classes = (IsAdminUser,)


class ProductSignAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductSign
    serializer_class = ProductSignSerializer
    permission_classes = (IsAdminUser,)


class ProductSignAPIRemove(generics.RetrieveDestroyAPIView):
    queryset = ProductsStorage.objects.all()
    serializer_class = ProductSignSerializer
    permission_classes = (IsAdminUser,)


class OrderCreateAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
