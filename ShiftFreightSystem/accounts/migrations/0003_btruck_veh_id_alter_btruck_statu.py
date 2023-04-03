# Generated by Django 4.1.7 on 2023-03-29 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '__first__'),
        ('accounts', '0002_btruck'),
    ]

    operations = [
        migrations.AddField(
            model_name='btruck',
            name='veh_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.vehicle'),
        ),
        migrations.AlterField(
            model_name='btruck',
            name='statu',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('None', 'None')], default='Pending', max_length=100),
        ),
    ]
