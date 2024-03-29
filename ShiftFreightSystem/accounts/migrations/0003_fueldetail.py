# Generated by Django 4.1.7 on 2023-05-08 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_fueldetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelDetail',
            fields=[
                ('fuel_id', models.AutoField(primary_key=True, serialize=False)),
                ('truck', models.CharField(max_length=50)),
                ('odometer_reading', models.CharField(max_length=6)),
                ('fill_date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.TextField()),
                ('bill_image', models.ImageField(upload_to='images/fuel_bills/')),
                ('added_driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
