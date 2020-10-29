# Generated by Django 3.1.2 on 2020-10-24 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('giohang', '0002_remove_giohang_gia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giohang',
            name='Don',
        ),
        migrations.AddField(
            model_name='giohang',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]