# Generated by Django 4.1.7 on 2023-02-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='business',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='ctype',
            field=models.CharField(default='', max_length=100),
        ),
    ]
