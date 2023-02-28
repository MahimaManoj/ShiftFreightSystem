from django.db import models

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
    driver_name = models.CharField(max_length=100)
    driver_address = models.CharField(max_length=200)
    driver_email = models.CharField(max_length=100, unique=True)
    driver_phone = models.BigIntegerField()
    driver_licence = models.CharField(max_length=100)
    driver_vehicle = models.ForeignKey(vehicle, verbose_name='register_no', on_delete=models.DO_NOTHING,default="")
    driver_image = models.ImageField()
    def __str__(self):
            return self.driver_name