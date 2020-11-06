from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',HomeView.as_view(),name = 'index'),
    path('login/',Login.as_view(),name = 'login'),
    path('logout/',Logout.as_view(),name = 'logout'),
    path('register/',Register.as_view(),name = 'register'),
    path('confirm/',Confirm.as_view(),name = 'confirm'),
    path('final/',Final.as_view(),name = 'final'),
    path('profile/<int:id>/',Profile.as_view(),name = 'profile'),
    path('cart/',cart ,name = 'cart'),
    path('update_item/',updateItem ,name = 'update_item'),
    path('checkout/<int:id>/',chekout,name = 'checkout'),


    path('orient-detail/',orientdetail,name = 'orient-detail'),
    path('citizen-detail/',citizendetail,name = 'citizen-detail'),
    path('cadino-detail/',candinodetail,name = 'candino-detail'),
    path('daniel-detail/',danieldetail,name = 'daniel-detail'),
    path('casio-detail/',casiodetail,name = 'casio-detail'),


    path('index-admin/',admin,name='admin'),
    path('product-admin/',proadmin,name='proadmin'),
    path('account-admin/',accadmin,name='accamin'),
    path('event-admin/',eventadmin,name='eventamin'),
    path('event/<int:id>',eventdetail,name='eventdetail'),
    path('addevent/<int:id>',addevent,name='addevent'),
    path('event-delete/<int:id>',deletevent,name='deletevent'),
    path('product-delete/<int:id>',deleteproduct,name='deletepro'),
    path('account-delete/<int:id>',deleteaccount,name='deleteaccount'),
    path('order-delete/<int:id>',deleteorder,name='deleleorder'),
    path('order-admin/',orderadmin,name='orderamin'),
    path('order-edit/<int:id>',orderedit,name='orderedit'),
    path('chart-admin/',chart,name='chartamin'),
    path('contact-admin/',contactadmin,name='contactamin'),
    path('contact-detail<int:id>/',contactdetail,name='contactdetail'),
    path('complete/',paymentComplete,name='complete'),
    path('product/',product,name='product'),
    path('contact/',contactuser,name='contact'),
    path('search/',search,name='search'),
    path('product-detail/<int:id>/',Productdetail.as_view(),name='product-detail'),
    path('delete-comment/<int:id>/<int:id_sp>/',delete,name='delete-comment'),
    path('orient/',orient,name='orient'),
    path('citizen/',citizen,name='citizen'),
    path('candino/',candino,name='candino'),
    path('daniel/',daniel,name='daniel'),
    path('casio/',casio,name='casio'),
    path('nam/',nam,name='nam'),
    path('nu/',nu,name='nu'),
    path('change_password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='reset_change_password/change_password_done.html'),
         name='password_change_done'),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name ='reset_change_password/change_password.html'),name='password_change'),

    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name ='reset_change_password/reset_password.html'),name ='reset_password'),

    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name ='reset_change_password/reset_password_sent.html'),name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name ='reset_change_password/reset_password_done.html'),name = 'password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
