# Generated by Django 3.2.12 on 2023-05-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ban_hang', '0008_alter_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sanpham',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
