from django.db import models
from sanpham.models import SanPham

# Create your models here.


class Anh(models.Model):
    SanPham = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    ChinhSua = models.DateField(auto_now=True)
    LoaiAnh = models.IntegerField(default=0)
    Anh = models.ImageField('pro_pictures ')

    def __str__(self):
        return str(self.SanPham)

    @property
    def imageURL(self):
        try:
            url = self.Anh.url
        except:
            url = ''
        return url