from django.db import models
from user.models import CustomerUser
from sanpham.models import SanPham

# Create your models here.


class DonHang(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    NgayDat = models.DateTimeField(auto_now_add=True)
    DaXuLy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class GiaoHang(models.Model):
    TenNguoiNhan = models.CharField(default='',max_length=100)
    DiaChi = models.CharField(default='',max_length=100)
    SoDienThoai = models.CharField(default='', max_length=15)
    DonHang = models.ForeignKey(DonHang,on_delete=models.CASCADE,null=True)


class ChiTietDon(models.Model):
    Don = models.ForeignKey(DonHang,on_delete=models.CASCADE)
    SanPham = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    SoLuong = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Don)

    @property
    def get_total(self):
        total = self.SanPham.Gia * self.SoLuong
        return total

    @property
    def get_doanhthu(self):
        total = sum([item.get_total for item in ChiTietDon.objects.all()])
        return total

class BinhLuan(models.Model):
    TieuDe = models.CharField(max_length=255,default='Bình Luận')
    Thich = models.IntegerField(default=0)
    KhongThich = models.IntegerField(default=0)
    Ngay = models.DateTimeField(auto_now_add=True)
    NoiDung = models.TextField(null=False)
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    SanPham = models.ForeignKey(SanPham,on_delete=models.CASCADE)
