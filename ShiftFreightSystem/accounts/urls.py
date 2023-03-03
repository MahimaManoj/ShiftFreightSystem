from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('Reg/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('driverlogin/',views.DriverLogin,name='driverlogin'),
    path('booking1/',views.Booking1,name='booking1'),
    path('booking2/',views.Booking2,name='booking2'),
    path('booking3/',views.Booking3,name='booking3'),

    # path('consignorReg/',views.ConsignorReg,name='ConsignorReg'),
    # path('commonmanReg/',views.CommonManReg,name='CommonManReg'),

]
