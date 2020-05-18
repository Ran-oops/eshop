from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible
from django.conf import settings

#在每个类里面加一个python_2_unicode_compatible装饰器可以保证在python2下的兼容性
@python_2_unicode_compatible
class Category(models.Model):
        """
        商品类别：笔记本，平板电脑，一体机，台式机，服务器
        """
        name = models.CharField(max_length=200)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

@python_2_unicode_compatible
class Manufacture(models.Model):
        """
        生产产商
        """
        name = models.CharField(max_length=200)
        description = models.TextField()
        logo=models.ImageField(blank=True, null=True, max_length=200, upload_to='manufacture/uploads/%Y/%m/%d/')
        created=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name



@python_2_unicode_compatible
class Product(models.Model):
    """
    产品
    """
    model = models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(max_length=200, upload_to='product/uploads/%Y/%m/%d/')
    price=models.DecimalField(max_digits=12, decimal_places=2)
    sold=models.PositiveIntegerField(default=0)
    category=models.









