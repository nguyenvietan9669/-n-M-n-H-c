# Generated by Django 3.1.2 on 2020-11-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0002_auto_20201017_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='SoLuongHang',
            field=models.IntegerField(default=0),
        ),
    ]
