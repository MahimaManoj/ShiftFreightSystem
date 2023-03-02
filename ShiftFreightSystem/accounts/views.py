from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Account
from django.contrib.auth import authenticate, login
from django.contrib import auth



# Create your views here.

# def ConsignorReg(request):
#     return render(request,'consignorReg.html')



def registration(request):
    if request.method == 'POST':
        role = request.POST['role']
        name=request.POST['name']
        address1=request.POST['address1']
        address2=request.POST['address2']
        city=request.POST['city']
        pincode=request.POST['pincode']
        district=request.POST['district']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        print('1')
        is_consignor = is_commonman = False
        if role =='is_consignor':
            is_consignor=True
        else:
            is_commonman=True

        if password==cpassword:
            # if Account.objects.filter(username=username).exists():
            #     messages.info(request,'username taken')
            #     print('3')
            #     return redirect('register/')
            # elif Account.objects.filter(email=email).exists():
            if Account.objects.filter(email=email).exists():

                # messages.info(request,'email already taken')
                return redirect('Reg/')
            else:
                user=Account.objects.create_user(email = email,
            name=name, 
            address1=address1,
            address2=address2,
            city=city,
            pincode=pincode,
            district = district,
            phone = phone,
            is_consignor=is_consignor,
            is_commonman=is_commonman )

            user.save()
            print(user)
            # messages.success(request, 'Thank you for registering with us. Please Login')
            return redirect('login')
        else:
              print("password is not matching")
    else:   
              # return redirect('index.html')
     return render(request,'Reg.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = ''
        try:
            role = Account.objects.get(email=email).role
        except Account.DoesNotExist:
            return HttpResponse("Invalid")
        print(email,password)
        user=authenticate(username=role, password=password)
        print(user)
        if user is not None:
            #login(user)
            auth.login(request, user)
            # save email in session
            request.session['email'] = email
            if user.is_admin:
                return redirect('http://127.0.0.1:8000/admin/')
            if user.is_consignor:
                return redirect('consignorhome')
            if user.is_commonman:
                return redirect('commonmanhome')
            elif user.is_driver:
                return redirect('driverhome')   
            else:
                return redirect('home')
        else:
            # messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'loginNew.html') 


def DriverLogin(request):
    return render(request,'driverlogin.html')



# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)
#         user=auth.authenticate(email=email,password=password)
#         print(user)
#         if user and user.is_active:
#             #login(user)
#             auth.login(request,user)
#             # save email in session
#             request.session['email'] = email
#             if user.is_admin:
#                 return redirect('/admin/')
#             if user.is_consignor:
#                 return redirect('consignorhome')
#             elif user.is_commonman:
#                 return redirect('http://127.0.0.1:8000/commonman/commonmanhome')
#             # elif user.is_driver:
#             #     return redirect('driverhome')    
#             else:
#                 return redirect('/')
#         else:
#             # messages.error(request, 'Invalid Credentials')
#             return redirect('login')
#     return render(request,'loginNew.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('login')