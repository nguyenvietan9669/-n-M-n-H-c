from django.db.models.functions import Extract

from sanpham.models import SanPham
from user.models import CustomerUser
from donhang.models import ChiTietDon
from donhang.models import DonHang
def thuonghieu1(id,sl):
    c = 0
    b = []
    sanpham = SanPham.objects.all()
    for item in sanpham:
        if item.ThuongHieu.id == id and c <= sl:
            c = c + 1
            b.append(item)
    return b


def sanphamhot(id,sl):
    c = 0
    b = []
    sanpham = SanPham.objects.all()
    for item in sanpham:
        if item.ThuongHieu.id == id and c <= sl and item.SanPham_Hot == True:
            c = c + 1
            b.append(item)
    return b

def timkiem(timkiem):
    tim = timkiem.lower()
    sanpham =[]
    product = SanPham.objects.all()
    for pro in product:
        ten = (pro.TenSanPham).lower()
        if ten.find(tim) >= 0:
            sanpham.append(pro)

    return sanpham


def xoagiohang(id):
    user = CustomerUser.objects.get(pk = id)
    giohang = user.giohang_set.all()
    for item in giohang:
        item.delete()


def themchitiet(id,id_don):
    user = CustomerUser.objects.get(id = id)
    donhang = DonHang.objects.get(id = id_don)
    giohang = user.giohang_set.all()
    for item in giohang:
        ChiTietDon.objects.create(Don = donhang,
                                  SanPham = item.SanPham,
                                  SoLuong = item.SoLuong)



def doanhthuthang(thang):
    tthang = 0
    months = DonHang.objects.all()
    for item in months:
        if item.NgayDat.month == thang:
            for it in item.chitietdon_set.all():
                tthang = tthang + it.SanPham.Gia * it.SoLuong

    return tthang