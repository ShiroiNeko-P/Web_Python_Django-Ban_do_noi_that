# Generated by Django 3.2.12 on 2023-05-29 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_ban_hang', '0034_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Like',
            field=models.ManyToManyField(default=0, related_name='like_blog', to=settings.AUTH_USER_MODEL),
        ),
    ]