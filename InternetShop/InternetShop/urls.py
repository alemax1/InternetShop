from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from InternetShop import settings
from InternetShopApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductsAPIList.as_view()),
    path('api/v1/products/<int:pk>/', ProductsAPIUpdate.as_view()),
    path('api/v1/productsremove/<int:pk>/', ProductsAPIRemove.as_view()),
    path('api/v1/storage/', StorageAPIList.as_view()),
    path('api/v1/storage/<int:pk>/', StorageAPIList.as_view()),
    path('api/v1/storageremove/<int:pk>/', StorageAPIList.as_view()),
    path('api/v1/productsign/', ProductSignAPIList.as_view()),
    path('api/v1/productsign/<int:pk>/', ProductSignAPIUpdate.as_view()),
    path('api/v1/productsignremove/<int:pk>/', ProductSignAPIRemove.as_view()),
    path('api/v1/order/', OrderCreateAPIList.as_view()),
    path('api/v1/login/', include('djoser.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
