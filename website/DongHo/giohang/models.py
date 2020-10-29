from django.db import models
from sanpham.models import SanPham
from user.models import CustomerUser

# Create your models here.

class GioHang (models.Model):
    User = models.ForeignKey(CustomerUser,on_delete=models.CASCADE,null=True)
    SanPham = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    SoLuong = models.IntegerField(default=0)

    def __str__(self):
        return str(self.User)

    @property
    def get_total(self):
        total = self.SanPham.Gia * self.SoLuong
        return total