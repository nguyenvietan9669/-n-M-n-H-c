from django.db import models
from sanpham.models import SanPham

# Create your models here.


class SuKien(models.Model):
    TieuDe = models.CharField(max_length=255,default='')
    Anh = models.ImageField('even_picture')
    MoTa = models.TextField
    TrangThai = models.BooleanField(default= True)


class ChiTiet_Sukien(models.Model):
    SuKien = models.ForeignKey(SuKien,on_delete=models.CASCADE)
    SanPham = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    NgayDang = models.DateField(auto_now_add=True)
