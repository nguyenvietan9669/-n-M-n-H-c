# Generated by Django 3.1.2 on 2020-10-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ketnoi', '0002_ketnoi_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ketnoi',
            name='NoiDung',
            field=models.TextField(default=''),
        ),
    ]
