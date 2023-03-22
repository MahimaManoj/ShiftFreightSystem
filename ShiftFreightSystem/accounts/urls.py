from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('Reg/',views.registration,name='registration'),
    path('viewlogin/',views.viewlogin,name='viewlogin'),
    path('driverlogin/',views.DriverLogin,name='driverlogin'),
    path('booking1/',views.Booking1,name='booking1'),
    path('booking2/',views.Booking2,name='booking2'),
    path('booking3/',views.Booking3,name='booking3'),
    path('book/',views.Book,name='book'),
    path('driverhome/',views.DriverHome,name='driverhome'),
    path('consignorhome/',views.ConsignorHome,name='consignorhome'),
    path('viewfuel/',views.ViewFuel,name='viewfuel'),
    path('driverprofile/',views.DriverProfile,name='driverprofile'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('addfuel/', views.AddFuel, name='addfuel'),
    path('driverbasic/', views.DriverBasic, name='driverbasic'),
    path('driverconsignment/', views.DriverConsignment, name='driverconsignment'),
    path('logout/', views.logout, name='logout'),
    path('consignorprofile/', views.ConsignorProfile, name='consignorprofile'),
     

    # path('consignorReg/',views.ConsignorReg,name='ConsignorReg'),
    # path('commonmanReg/',views.CommonManReg,name='CommonManReg'),

]
