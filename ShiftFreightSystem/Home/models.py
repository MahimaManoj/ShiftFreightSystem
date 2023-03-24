from django.db import models
from accounts.models import Account

# Create your models here.

class vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    register_no=models.CharField(max_length=100)
    regd_owner=models.CharField(max_length=100)
    reg_address=models.CharField(max_length=100)
    makers_class=models.CharField(max_length=100)
    vehicle_class=models.CharField(max_length=100)
    fuel=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    insurance=models.CharField(max_length=100)
    def __str__(self):
            return self. register_no

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100,default='')
    driver_address = models.CharField(max_length=200,default='')
    driver_email = models.CharField(max_length=100, unique=True,default='')
    driver_phone = models.BigIntegerField(unique=True,default=0)
    driver_licence = models.CharField(max_length=100,default='')
    acc = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
   
    def __str__(self):
            return self.driver_name
    

# class AddFuel(models.Model):
#     fuel_id = models.AutoField(primary_key=True)
#     vehicle_id = models.ForeignKey(vehicle, on_delete=models.CASCADE)
#     driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
#     fuel_quantity = models.CharField(max_length=200)
#     odometer_reading = models.CharField(max_length=200)
#     fill_date = models.DateField()
#     amount = models.CharField(max_length=200)
#     comment = models.CharField(max_length=200)
#     def __str__(self):
#             return self.fuel_id



