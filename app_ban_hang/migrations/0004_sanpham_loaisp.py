# Generated by Django 3.2.12 on 2023-05-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ban_hang', '0003_auto_20230516_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='LoaiSP',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]