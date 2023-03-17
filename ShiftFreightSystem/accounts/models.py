from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin, AbstractUser
import datetime


class MyAccountManager(BaseUserManager):
    def create_user(self,name,address1,address2,city,pincode,district,state,phone,email,is_consignor,password=None):

        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email = self.normalize_email(email),
            name=name, 
            address1=address1,
            address2=address2,
            city=city,
            pincode=pincode,
            district = district,
            state=state,
            phone = phone,
            is_consignor=is_consignor,


        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,password,email,**extra_fields):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password, **extra_fields
        
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    
class Account(AbstractBaseUser,PermissionsMixin):
    status_choices=(('Approved','Approved'),('Pending','Pending'), ('None','None'))
    role_choices=(('is_admin','is_admin'),('is_consignor','is_consignor'),('is_driver','is_driver'))
    district_choices=(
        ('Kozhikode','Kozhikode'),
        ('Malappuram','Malappuram'),
        ('Kannur','Kannur'),
        # ('Trivandrum','Trivandrum'),
        ('Palakkad','Palakkad'),
        ('Thrissur','Thrissur'),
        ('Kottayam','Kottayam'),
        ('Alappuzha','Alappuzha'),
        ('Idukki','Idukki'),
        ('Kollam','Kollam'), 
        ('Ernakulam','Ernakulam'),
        ('Wayanad','Wayanad'),
        ('Kasaragod','Kasaragod'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Thiruvananthapuram','Thiruvananthapuram'),
        ('None','None'),
    )


    id            = models.AutoField(primary_key=True)
    name          = models.CharField(max_length=100, default='')
    phone         = models.BigIntegerField(default=0)
    email         = models.EmailField(max_length=100, unique=True)
    address1      = models.CharField(max_length=100, default='')
    address2      = models.CharField(max_length=100, default='')
    city          = models.CharField(max_length=100, default='')
    state          = models.CharField(max_length=100, default='')
    district      = models.CharField(max_length=50,choices=district_choices,default='None')
    pincode       = models.BigIntegerField(default=0)
    role          = models.CharField(max_length=100,choices=role_choices)
    
    # dob           = models.DateField(blank=True,null=True)
    # gender        = models.CharField(max_length=50,choices=gender_choices,default='None')
    

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_consignor      = models.BooleanField(default=False)
    is_driver      = models.BooleanField(default=False)
    

    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False) 
    is_superadmin     = models.BooleanField(default=False) 


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'address1','address2','city','state','pincode','district','is_consignor']
    # REQUIRED_FIELDS = [,'password']


    objects = MyAccountManager()

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    

