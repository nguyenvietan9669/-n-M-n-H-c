from django.db import models

# Create your models here.


class GioiTinh(models.Model):
    TenGioiTinh = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.TenGioiTinh


class ThuongHieu(models.Model):
    TenThuongHieu = models.CharField(max_length=255,default='')
    MoTa = models.TextField(default='')
    Anh = models.ImageField('tra_pictures ')

    def __str__(self):
        return self.TenThuongHieu

    @property
    def get_tile(self):
        tile = 0
        sanpham = self.sanpham_set.all()
        for i in sanpham:
            chitiet = i.chitietdon_set.all()
            for item in chitiet:
                tile = tile+ item.SoLuong
        sp = SanPham.objects.all()
        total = 0
        for it in sp:
            for chi in it.chitietdon_set.all():
                total = total+chi.SoLuong
        if total != 0:
            return tile/total*100





class ThongTin(models.Model):
    XuatXu = models.CharField(max_length=255,default='')
    May = models.CharField(max_length=255,default='')
    BaoHanh = models.CharField(max_length=255,default='')
    DayDeo = models.CharField(max_length=255,default='')
    ChongNuoc = models.CharField(max_length=255,default='')
    DuongKinh = models.CharField(max_length=255,default='')
    MatKinh = models.CharField(max_length=255,default='')


class SanPham(models.Model):
    TenSanPham = models.CharField(max_length=255,default='')
    GioiTinh = models.ForeignKey(GioiTinh,on_delete=models.CASCADE)
    ThuongHieu = models.ForeignKey(ThuongHieu,on_delete=models.CASCADE)
    MoTa = models.TextField(default='')
    SanPham_GiamGia = models.BooleanField(default=False)
    SanPham_Hot = models.BooleanField(default=False)
    Gia = models.IntegerField(default=0)
    Gia_Giam = models.IntegerField(default=0)
    ThongTin = models.ForeignKey(ThongTin,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.TenSanPham