from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from InternetShop import settings
from InternetShopApp.views import *

router = routers.DefaultRouter()
router.register(r'products/', ProductsViewSet, basename="products")
router.register(r'storage/', StorageViewSet, basename="storage")
router.register(r'productsign/', ProductSignViewSet, basename="productsign")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/order/', OrderCreateAPIList.as_view()),
    path('api/v1/login/', include('djoser.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
