from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User



# Create your views here.

# def ConsignorReg(request):
#     return render(request,'consignorReg.html')
# def CommonManReg(request):
#     return render(request,'commonManReg.html')


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
        print(email,password)
        user=authenticate(email=email,password=password)
        print(user)
        if user is not None:
            #login(user)
            auth.login(request, user)
            # save email in session
            request.session['email'] = email
            if user.is_admin:
                return redirect('http://127.0.0.1:8000/admin/')
            if user.is_consignor:
                return redirect('Consignor/consignorhome')
            if user.is_commonman:
                return redirect('commonman')
            elif user.is_driver:
                return redirect('driverhome')    
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'loginNew.html')
