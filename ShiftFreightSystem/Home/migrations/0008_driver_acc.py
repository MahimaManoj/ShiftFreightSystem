# Generated by Django 4.1.7 on 2023-03-24 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0007_remove_driver_driver_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='acc',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
