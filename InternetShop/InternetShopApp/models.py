from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, unique=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    hashtag = models.CharField(max_length=255)
    is_hit = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductsStorage(models.Model):
    product_price = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    product = models.ForeignKey('Products', on_delete=models.PROTECT, null=True)
    product_size = models.ForeignKey('ProductsSize', on_delete=models.PROTECT, null=True)
    product_sign = models.ForeignKey('ProductSign', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product_price


class ProductsSize(models.Model):
    size = models.CharField(max_length=255)
    demensional_grid = models.ForeignKey('DemensionalGridTypes', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.size


class ProductSign(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class DemensionalGridTypes(models.Model):
    values = models.CharField(max_length=255)

    def __str__(self):
        return self.values
    
    
class Order(models.Model):
    full_name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
