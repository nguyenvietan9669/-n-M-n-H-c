# Generated by Django 3.1.2 on 2020-10-17 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sanpham', '0002_auto_20201017_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThongTinG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenNguoiNhan', models.CharField(default='', max_length=100)),
                ('DiaChi', models.CharField(default='', max_length=100)),
                ('SoDienThoai', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NgayDat', models.DateTimeField(auto_now_add=True)),
                ('DaXuLy', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BinhLuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TieuDe', models.CharField(default='Bình Luận', max_length=255)),
                ('Thich', models.IntegerField(default=0)),
                ('KhongThich', models.IntegerField(default=0)),
                ('Ngay', models.DateTimeField(auto_now_add=True)),
                ('NoiDung', models.TextField()),
                ('SanPham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.sanpham')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
