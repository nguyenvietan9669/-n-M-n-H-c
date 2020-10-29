import random

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.views import View
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from user.models import CustomerUser
from sanpham.models import *
from sukien.models import *
from donhang.models import GiaoHang
from giohang.models import GioHang
from ketnoi.models import KetNoi
from django.contrib import messages
from donhang.models import BinhLuan
from django.core.paginator import Paginator
from .core import *
from django.db.models import Count


# Create your views here.


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            user, created = CustomerUser.objects.get_or_create(username = user)
            tongitem = user.get_cart_items
        else:
            donhang = {'get_cart_total': 0, 'get_cart_items': 0}
            tongitem = donhang['get_cart_items']
        thuonghieu = ThuongHieu.objects.all()
        sanpham = thuonghieu1(1,2)
        sanpham1 = thuonghieu1(2,2)
        sanpham2 = thuonghieu1(3,2)
        sanpham3 = thuonghieu1(4,2)
        sanpham4 = thuonghieu1(5,2)
        hot = sanphamhot(1,2)
        hot1 = sanphamhot(2,2)
        hot2 = sanphamhot(3,2)
        hot3 = sanphamhot(4,2)
        hot4 = sanphamhot(5,2)

        content = {
            'tongitem':tongitem,
            'thuonghieu':thuonghieu,
            'sanpham':sanpham,
            'sanpham1':sanpham1,
            'sanpham2':sanpham2,
            'sanpham3':sanpham3,
            'sanpham4':sanpham4,
            'hot':hot,
            'hot1':hot1,
            'hot2':hot2,
            'hot3':hot3,
            'hot4':hot4,
        }

        return render(request, 'cuahang/home.html',content)



class Login(View):
    def get(self, request):
        return render(request,'login/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_staff == False:
                login(request,user)
                return redirect('index')
            else:
                login(request, user)
                return redirect('admin')
        else:
            messages.error(request,'Thông tin tài khoản hoặc mật khẩu không chính xác')
            return redirect('login')


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/')

# -------------------------------Register--------------------------------------------------
class Register(View):
    def get(self, request):
        return render(request, 'login/register.html')

    def post(self, request):
        danhsachso = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ma = random.choices(danhsachso, k=6)
        ma = ''.join(ma)
        template = render_to_string('login/template_email.html', {'name': request.POST['first'], 'ma': ma})
        email = request.POST['email']
        first = request.POST['first']
        last = request.POST['last']
        address = request.POST['address']
        birth = request.POST['birth']
        phone = request.POST['phone']
        e = str(email)
        cus = CustomerUser.objects.filter(email=e)
        if cus is None:
            email = EmailMessage(
                'Thư gửi mã xác nhận',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.fail_silently = False
            email.send()
            content = {
                'email': e,
                'ma': ma,
                'first': first,
                'last': last,
                'address': address,
                'birth': birth,
                'phone': phone
            }
            return render(request, 'login/confirm_email.html', content)
        else:
            messages.error(request, 'Email đã được dùng để đăng ký cho tài khoản khác')
            return render(request, 'login/register.html')


class Confirm(View):
    def post(self, request):
        ma = request.POST['ma']
        email = request.POST['email']
        first = request.POST['first']
        last = request.POST['last']
        address = request.POST['address']
        birth = request.POST['birth']
        phone = request.POST['phone']
        content = {
            'email': email,
            'ma': ma,
            'first': first,
            'last': last,
            'address': address,
            'birth': birth,
            'phone': phone
        }
        if ma != request.POST['confirm']:
            messages.error(request, 'Mã xác nhận không đúng')
            return render(request, 'login/confirm_email.html', content)
        else:
            return render(request, 'login/continue.html', content)


class Final(View):
    def post(self, request):
        user = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['re-password']
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        address = request.POST['address']
        birth = request.POST['birth']
        phone = request.POST['phone']
        content = {
            'email': email,
            'first': first,
            'last': last,
            'address': address,
            'birth': birth,
            'phone': phone
        }
        if password != repassword:
            messages.error(request, 'Mật khẩu không trùng khớp mời nhập lại ')
            return render(request, 'login/continue.html', content)
        else:
            my_user = CustomerUser.objects.create_user(username=user, email=email)
            my_user.set_password(password)
            my_user.first_name = first
            my_user.last_name = last
            my_user.phone = phone
            my_user.address = address
            my_user.birthdate = birth
            my_user.save()
            messages.success(request, 'Đăng ký thành công ,Mời bạn đăng nhập')
            return render(request, 'login/login.html')

# --------------------------------End Register-------------------------------------------


#product
def product(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.all()
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content ={'product':pro,'tongitem':tongitem}
    return render(request,'cuahang/products.html',content)


def orient(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(ThuongHieu = 1)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Orient.html', content)


def citizen(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(ThuongHieu = 2)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Citizen.html', content)

def candino(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(ThuongHieu = 3)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Candino.html', content)


def daniel(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(ThuongHieu = 4)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Danielwellington.html', content)

def casio(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(ThuongHieu = 5)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Casio.html', content)

def nam(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(GioiTinh = 1)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Nam.html', content)

def nu(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
    pro = SanPham.objects.filter(GioiTinh = 2)
    paginator = Paginator(pro, 9)
    page = request.GET.get('page')
    pro = paginator.get_page(page)
    content = {'product': pro, 'tongitem': tongitem}
    return render(request, 'category/Nu.html', content)
#end-product---

#giohang
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        items = user.giohang_set.all()
        tongitem = user.get_cart_items
    else:
        items =[]
        user ={'get_cart_total':0,'get_cart_items':0}
        tongitem = user['get_cart_items']
    context = {'items':items,'donhang':user,'tongitem':tongitem}
    return render(request,'giohang/cart.html',context)


def chekout(request,id):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        items = user.giohang_set.all()
        tongitem = user.get_cart_items
        Cus = CustomerUser.objects.get(pk=id)
        usd = (user.get_cart_total) / 23176
    else:
        items = []
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
        usd = (user.get_cart_total)/23000
    context = {'items': items, 'donhang': user,'cus':Cus,'tongitem':tongitem,'usd':usd}
    return render(request,'giohang/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('productId:', productId)

    user = request.user
    product = SanPham.objects.get(id=productId)
    user , created = CustomerUser.objects.get_or_create(username= user)

    orderItem, created = GioHang.objects.get_or_create(User = user , SanPham = product)

    if action == 'add':
        orderItem.SoLuong = (orderItem.SoLuong + 1)
    elif action == 'remove':
        orderItem.SoLuong = (orderItem.SoLuong - 1)
    orderItem.save()

    if orderItem.SoLuong <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe=False)


class Profile(View):
    def get(self,request,id):
        Cus = CustomerUser.objects.get(pk=id)
        return render(request,'profile/profile.html',{'user': Cus})



class Productdetail(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            user = request.user
            user, created = CustomerUser.objects.get_or_create(username=user)
            tongitem = user.get_cart_items
            pro = SanPham.objects.get(pk=id)
            image = pro.anh_set.all()
            bl = pro.binhluan_set.all()
        else:
            pro = SanPham.objects.get(pk=id)
            image = pro.anh_set.all()
            bl = pro.binhluan_set.all()
            user = {'get_cart_total': 0, 'get_cart_items': 0}
            tongitem = user['get_cart_items']
        content = {"product":pro,"anh":image,"tongitem":tongitem,"binhluan":bl}
        return render(request,'cuahang/product-detail.html',content)

    def post(self,request,id):
            pro_id = id
            pro = SanPham.objects.get(pk = id)
            if pro_id:
                noidung = request.POST.get('context')
                comment = BinhLuan.objects.create(user=request.user,
                                                  SanPham = pro,
                                                  NoiDung = noidung
                                                  )
                comment.save()
            return redirect('product-detail',id = id)

def search(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = CustomerUser.objects.get_or_create(username=user)
        tongitem = user.get_cart_items
        tim = request.GET.get('Search')
        pro = timkiem(tim)
    else:
        user = {'get_cart_total': 0, 'get_cart_items': 0}
        tongitem = user['get_cart_items']
        tim = request.GET.get('Search')
        pro = timkiem(tim)
    content = {"product": pro,'donhang':user,'tongitem':tongitem,"tim":tim}
    return render(request,'cuahang/search.html',content)


def delete(request,id,id_sp):
    comment = BinhLuan.objects.get(id = id)
    comment.delete()
    return redirect('product-detail',id = id_sp )


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:',body)
    user = CustomerUser.objects.get(id = body['userId'])
    donhang = DonHang.objects.create(
        user = user
    )
    GiaoHang.objects.create(
        TenNguoiNhan = body['shippingname'],
        DiaChi = body['shippingaddress'],
        SoDienThoai = body['shippingphone'],
        DonHang=donhang,
    )
    themchitiet(body['userId'],donhang.id)
    xoagiohang(body['userId'])

    return JsonResponse('Payment submitted..', safe=False)


def admin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        donhang = DonHang.objects.all()
        user = CustomerUser.objects.all()
        thuonghieu = ThuongHieu.objects.all()
        thanthiet = CustomerUser.objects.values('username','last_name','first_name','birthdate')\
        .annotate(dcount=Count('donhang')).order_by('-dcount').all()[:5]
        sanphambanchay = SanPham.objects.values('TenSanPham').annotate(dcount = Count('chitietdon'))\
        .order_by('-dcount').all()[:5]
        chitiet = ChiTietDon.objects.get(id=1)
        content = {"donhang":donhang,
                   "tk":user,
                   "chitiet":chitiet,
                   "thanthiet":thanthiet,
                   "chay":sanphambanchay,
                   "thuonghieu":thuonghieu}
        return render(request,'Admin/trangchu.html',content)



def proadmin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        sanpham = SanPham.objects.all()
        paginator = Paginator(sanpham, 9)
        page = request.GET.get('page')
        sanpham = paginator.get_page(page)
        context = {"sanpham":sanpham}
        return render(request,'Admin/admin-product.html',context)

def accadmin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        taikhoan = CustomerUser.objects.all()
        paginator = Paginator(taikhoan, 9)
        page = request.GET.get('page')
        taikhoan = paginator.get_page(page)
        context = {"taikhoan":taikhoan}
        return render(request,'Admin/admin-account.html',context)


def eventadmin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        sukien = SuKien.objects.all()
        paginator = Paginator(sukien, 9)
        page = request.GET.get('page')
        sukien = paginator.get_page(page)
        context = {"sukien":sukien}
        return render(request,'Admin/admin-event.html',context)


def orderadmin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        donhang = DonHang.objects.all()
        paginator = Paginator(donhang, 9)
        page = request.GET.get('page')
        donhang = paginator.get_page(page)
        context = {"donhang":donhang}
        return render(request,'Admin/admin-order.html',context)


def contactadmin(request):
    if request.user.is_staff == False:
        return redirect('index')
    else:
        phanhoi = KetNoi.objects.all()
        paginator = Paginator(phanhoi, 9)
        page = request.GET.get('page')
        phanhoi = paginator.get_page(page)
        context = {"phanhoi":phanhoi}
        return render(request,'Admin/admin-contact.html',context)