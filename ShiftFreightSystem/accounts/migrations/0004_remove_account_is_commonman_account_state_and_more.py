# Generated by Django 4.1.7 on 2023-03-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_account_groups_remove_account_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_commonman',
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('is_admin', 'is_admin'), ('is_consignor', 'is_consignor'), ('is_driver', 'is_driver')], max_length=100),
        ),
    ]