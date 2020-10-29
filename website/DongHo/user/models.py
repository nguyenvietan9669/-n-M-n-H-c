from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    phone = models.CharField(default='', max_length=15)
    address = models.CharField(default='', max_length=255)
    birthdate = models.DateField(auto_now_add=True)


    @property
    def get_cart_total(self):
        giohang = self.giohang_set.all()
        total = sum([item.get_total for item in giohang])
        return total

    @property
    def get_cart_items(self):
        giohang = self.giohang_set.all()
        total = sum([item.SoLuong for item in giohang])
        return total
