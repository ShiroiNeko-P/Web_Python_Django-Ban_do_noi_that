# Generated by Django 3.2.12 on 2023-06-01 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_ban_hang', '0037_auto_20230530_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Like',
            field=models.ManyToManyField(null=True, related_name='like_blog', to=settings.AUTH_USER_MODEL),
        ),
    ]