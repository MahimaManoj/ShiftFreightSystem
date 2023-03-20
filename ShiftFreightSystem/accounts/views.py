from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Account
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail



# Create your views here.

# def ConsignorReg(request):
#     return render(request,'consignorReg.html')


def DriverHome(request):
    return render(request,'driverhome.html')

def ConsignorHome(request):
    return render(request,'consignorhome.html')



def registration(request):
    if request.method == 'POST':
        name=request.POST['name']
        address1=request.POST['address1']
        address2=request.POST['address2']
        city=request.POST['city']
        pincode=request.POST['pincode']
        district=request.POST['district']
        state=request.POST['state']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        print('1')
        is_consignor = True
        
            

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
            state=state,
            pincode=pincode,
            district = district,
            phone = phone,
            password=password,
            is_consignor=is_consignor,
        )

            user.save()
            print(user)
            # messages.success(request, 'Thank you for registering with us. Please Login')
            return redirect('viewlogin')
        else:
              print("password is not matching")
    else:   
              # return redirect('index.html')
     return render(request,'Reg.html')



def viewlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user=auth.authenticate(email=email, password=password)
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
            elif user.is_driver:
                return redirect('driverhome')   
            else:
                return redirect('home')
        else:
            # messages.error(request, 'Invalid Credentials')
            return redirect('viewlogin')
    return render(request, 'loginNew.html') 


def DriverHome(request):
    if request.user.is_authenticated:
        if request.user.is_driver:
            email = request.session.get('email')

    return render(request, 'driverhome.html')

def ConsignorHome(request):
    if request.user.is_authenticated:
        if request.user.is_consignor:
            email = request.session.get('email')

    return render(request, 'consignorhome.html')


def DriverLogin(request):
    return render(request,'driverlogin.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('login')


def Book(request):
    return render(request,'book.html')

def Booking1(request):
    return render(request,'booking1.html')

def Booking2(request):
    return render(request,'booking2.html')

def Booking3(request):
    return render(request,'booking3.html')

def ViewFuel(request):
    return render(request,'viewfuel.html')

def AddFuel(request):
    return render(request,'addfuel.html')

def DriverProfile(request):
    return render(request,'driverprofile.html')

def DriverBasic(request):
    return render(request,'driverbasic.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email

            current_site = get_current_site(request)
            message = render_to_string('ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'jobportalajce@gmail.com',
                [email],
                fail_silently=False,
            )
            
            # messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('viewlogin')
        else:
            # messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'Forgot_Password.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        # messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        # messages.error(request, 'This link has been expired!')
        return redirect('viewlogin')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            # messages.success(request, 'Password reset successful')
            return redirect('viewlogin')
        else:
            # messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'ResetPassword.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('viewlogin')
    else:
        # messages.error(request, 'Invalid activation link')
        return redirect('register')


def DriverConsignment(request):
    return render(request,'driverconsignment.html')

