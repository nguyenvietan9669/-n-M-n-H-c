from django.contrib import admin
from user.models import CustomerUser
from anh.models import Anh
from donhang.models import DonHang, BinhLuan,GiaoHang,ChiTietDon
from giohang.models import GioHang
from ketnoi.models import KetNoi
from sanpham.models import ThongTin,SanPham,ThuongHieu,GioiTinh
from sukien.models import SuKien,ChiTiet_Sukien


# Register your models here.

admin.site.register(CustomerUser)
admin.site.register(Anh)
admin.site.register(DonHang)
admin.site.register(ChiTietDon)
admin.site.register(GiaoHang)
admin.site.register(ThuongHieu)
admin.site.register(GioiTinh)
admin.site.register(BinhLuan)
admin.site.register(GioHang)
admin.site.register(KetNoi)
admin.site.register(ThongTin)
admin.site.register(SanPham)
admin.site.register(SuKien)
admin.site.register(ChiTiet_Sukien)
