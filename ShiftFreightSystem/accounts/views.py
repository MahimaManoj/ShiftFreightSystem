from pyexpat.errors import messages
from django.shortcuts import redirect, render

from Home.models import vehicle
from Home.models import CompanyTruck
from .models import Account, BTruck
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
import random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from twilio.rest import Client
from random import randint
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json
from django.http import HttpResponse

ENDPOINT = "https://api.postalpincode.in/pincode/"
PIN_START = str(670001)
PIN_END = str(695615)


# sample phone number and driver information
# driver_info = {'name': 'John Doe', 'phone_number': '6238452'}

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
                return HttpResponse("<script>alert('Login Successful.');window.location='/accounts/adminfreight';</script>")
                # return redirect('adminfreight')
            if user.is_consignor:
                return HttpResponse("<script>alert('Login Successful.');window.location='/accounts/consignorhome';</script>")
                # return redirect('consignorhome')
            else:
                return redirect('home')
        else:
            return HttpResponse("<script>alert('Login Failed. Provide valid email and password.');window.location='/accounts/viewlogin';</script>")

            # messages.error(request, 'Invalid Credentials')

    return render(request, 'loginNew.html') 


# def DriverHome(request):
#     if request.user.is_authenticated:
#         if request.user.is_driver:
#             email = request.session.get('email')

#     return render(request, 'driverhome.html')

def ConsignorHome(request):
    if request.user.is_authenticated:
        if request.user.is_consignor:
            email = request.session.get('email')

    return render(request, 'consignorhome.html')




# def logout(request):
#     auth.logout(request)
#     return redirect('login')


def Book1(request):
    if request.method == 'POST':
        user = request.user
        p_cit=request.POST.get('p_cit')
        p_addres1=request.POST['p_addres1']
        p_addres2=request.POST['p_addres2']
        p_distric=request.POST['p_distric']
        p_stat=request.POST['p_stat']
        p_pincod=request.POST['p_pincod']
        d_cit=request.POST['d_cit']
        d_addres1=request.POST['d_addres1']
        d_addres2=request.POST['d_addres2']
        d_distric=request.POST['d_distric']
        d_stat=request.POST['d_stat']
        d_pincod=request.POST['d_pincod']
        good_typ=request.POST['good_typ']
        bookingdat=request.POST['bookingdat']
        weigh=request.POST['weigh']
        service=request.POST.getlist('service')
        load_descriptio=request.POST['load_descriptio']

        pincode = p_pincod or d_pincod
        
        if request.method == 'POST':
            pincode = request.POST.get('pincode')
            if pincode >= PIN_START and pincode <= PIN_END:
                response = requests.get(ENDPOINT + pincode)
                pincode_information = json.loads(response.text)
                information = pincode_information[0]['PostOffice'][0]
                data = {}
                for key, value in information.items():
                    if key == 'Name' or key == 'District':
                        data[key] = value
                # return HttpResponse(json.dumps(data))
                return data 
            if (pincode == p_pincod):
                return p_pincod 
            elif(pincode == d_pincod):
                return d_pincod 
            
                # raise ValueError("Pincode not valid. Enter a pincode existing in Kerala.")

            btr = BTruck.objects.create(
                us_id = user,
                p_cit=p_cit,
                p_addres1=p_addres1,
                p_addres2= p_addres2,
                p_distric=p_distric,
                p_stat=p_stat,
                p_pincod=p_pincod,
                d_cit=d_cit,
                d_addres1=d_addres1,
                d_addres2=d_addres2,
                d_distric=d_distric,
                d_stat=d_stat,
                d_pincod=d_pincod,
                good_typ=good_typ,
                bookingdat=bookingdat,
                weigh=weigh,
                service=service,
                load_descriptio=load_descriptio
            )
            btr.save()
            return HttpResponse("<script>alert('Booking successfully.');window.location='/accounts/viewbooking/';</script>")

    return render(request,'book.html')



def Booking1(request):

    return render(request,'booking1.html')

def Booking2(request):

    return render(request,'booking2.html')

def Booking3(request):

    return render(request,'booking3.html')

def ViewBooking(request):
    user=request.user.id
    vbt = BTruck.objects.filter(us_id=user)
    return render(request,'viewbooking.html',{'vbt':vbt})

def addtruckdriver(request,boo_id):
    btr=BTruck.objects.get(boo_id=boo_id)
    id=boo_id
    print(id)
    if request.method == 'POST':
        df = request.POST.get("adddr")
        tf = request.POST.get("addtr")
        print("demo",df,tf)
        if df:
           dff=Account.objects.get(id=df)
           df_id=dff.id
           print("$$$$$$$$$$$$$$$$$$$",df_id)
        else:
           df_id = None   

        if tf:
           veh=CompanyTruck.objects.get(truck_id=tf)
           tf_id=veh.truck_id
           print("$$$$$$$$$$$$$$$$$$$",tf_id)   
       
        if not BTruck.objects.filter(dr_id=df,veh_id=tf).exists():
            bb=BTruck.objects.get(boo_id=boo_id)
            dff=Account.objects.get(id=df_id)
            tff=CompanyTruck.objects.get(truck_id=tf_id)
            bb.veh_id=tff
            bb.dr_id=dff
            bb.save()
            
        else:
            if  BTruck.objects.filter(dr_id=df).exists():
              return HttpResponse("<script>alert('Driver on duty.');window.location='/accounts/addtruckdriver';</script>")
            elif  BTruck.objects.filter(veh_id=tf).exists():
              return HttpResponse("<script>alert('Vehicle on road.');window.location='/accounts/addtruckdriver';</script>")
            else:
                None
           

    ve = CompanyTruck.objects.all()
    tt = Account.objects.filter(is_driver = True)
    return render(request, 'addtruckdriver.html',{'tt':tt,'ve':ve,'id':id})

def BookingSummary(request,boo_id):
    bs = BTruck.objects.filter(boo_id=boo_id)
    btr=BTruck.objects.get(boo_id=boo_id)
    idd=boo_id
    print(idd)
    return render(request,'bookingsummary.html',{'bs':bs,"idd":idd})

def AdminFreight(request):
    us=Account.objects.filter(is_consignor=True)
    users = us.count()
    book = BTruck.objects.count()
    truck = CompanyTruck.objects.count()
    driver = Account.objects.filter(is_driver=True)
    drivers = driver.count()
    return render(request, 'adminfreight.html',{'users':users,'book':book,'truck':truck,'drivers':drivers})

def AdminBooking(request):
    ab = BTruck.objects.all()
    return render(request,'adminbooking.html',{'ab':ab})

def AdminProfile(request):
    cp = Account.objects.filter(id=request.user.id)
    return render(request,'adminprofile.html',{'cp':cp})


def AddFuell(request):
    # dr = Driver.objects.all()
    # if request.method == 'POST':
    #     user = request.user
    #     regno=request.POST['regno']
    #     drivername=request.POST.get('drivername')
    #     fuel_quantity=request.POST['fuel_quantity']
    #     odometer_reading=request.POST['odometer_reading']
    #     fill_date=request.POST['fill_date']
    #     amount=request.POST['amount']
    #     comment=request.POST['comment']
    #     af = AddFuel.objects.create(
    #         user_id=user,
    #         vehicle_id=regno,
    #          driver_id = drivername,
    #          fuel_quantity=fuel_quantity,
    #          odometer_reading=odometer_reading,
    #          fill_date=fill_date,
    #          amount=amount,
    #          comment=comment
    #     )
        # af.save()
        # return HttpResponse("<script>alert('Fuel added successfully.');window.location='/accounts/viewfuel/';</script>")
    
        return render(request,'addfuel.html')

def AddFuelDemo(request):
    return render(request,'addfueldemo.html')

def ViewFuel(request):
    return render(request,'viewfuel.html')

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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth.logout(request)
    return redirect('viewlogin')  


def DriverConsignment(request):
    return render(request,'driverconsignment.html')

def ConsignorProfile(request):
    
    cp = Account.objects.filter(id=request.user.id)
    return render(request,'consignorprofile.html',{'cp':cp})



# @csrf_exempt
# def send_otp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         otp = str(randint(100000, 999999))  # generate a 6-digit OTP
#         message = f'Your OTP is {otp}. Do not share it with anyone.'
#         try:
#             # replace with your Twilio phone number and sender ID
#             client.messages.create(to=phone_number, from_='your_twilio_phone_number_here', body=message)
#             return JsonResponse({'status': 'success', 'message': 'OTP sent successfully.'})
#         except:
#             return JsonResponse({'status': 'error', 'message': 'Failed to send OTP. Please try again later.'})
        

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from twilio.rest import Client
from random import randint

# replace with your account SID and auth token
# account_sid = ''
# auth_token = ''
# client = Client(account_sid, auth_token)

# @csrf_exempt
# def send_otp(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         otp = str(randint(100000, 999999))  # generate a 6-digit OTP
#         message = f'Your OTP is {otp}. Do not share it with anyone.'
#         try:
#             # replace with your Twilio phone number and sender ID
#             client.messages.create(to=phone_number, from_='your_twilio_phone_number_here', body=message)
#             return JsonResponse({'status': 'success', 'message': 'OTP sent successfully.'})
#         except:
#             return JsonResponse({'status': 'error', 'message': 'Failed to send OTP. Please try again later.'})



# def generate_otp():
#     otp = random.randint(100000, 999999)
#     return otp


# function to send OTP via SMS
# def send_otp_via_sms(phone_number, otp):
#     print(f'Sending OTP {otp} to {phone_number} via SMS...')

# # function to verify OTP
# def verify_otp(otp, user_input):
#     if str(otp) == user_input:
#         return True
#     else:
#         return False

# # main function for OTP login
# def otp_login(driver_info):
#     phone_number = driver_info['phone_number']
#     otp = generate_otp()
#     send_otp_via_sms(phone_number, otp)
#     user_input = input('Enter OTP received via SMS: ')
#     if verify_otp(otp, user_input):
#         print(f'Welcome {driver_info["name"]}!')
#     else:
#         print('Invalid OTP. Please try again.')

# # test OTP login function
# otp_login(driver_info)


# def Driverlog(request):
#     if request.method == 'POST':
#         phone_number = request.POST['phone_number']
#         print(phone_number)
#         user=auth.authenticate(phone=phone_number)
#         print(user)

#         if user is not None:
#             #login(user)
#             auth.login(request, user)
#             # save email in session
#             request.session['phone_number'] = phone_number

#             if user.is_driver:
#                 return redirect('driverhome')
#             else:
#                 return redirect('drlog')
#         else:
#             # messages.error(request, 'Invalid Credentials')
#             return redirect('drlog') 

#     return render(request,'drlog.html')



def Driverlog(request):
    if request.method == 'POST':
        user=request.user
        print(user)
        phone_number = request.POST['phone_number']
        print(phone_number)
        if(Account.objects.filter(phone=phone_number)):
            log=Account.objects.filter(phone=phone_number).values('role').get()['role']
            print(log)
            if log == 'is_driver':
            #    a=Driver.objects.create(acc=user,driver_phone=phone_number)  
            #    a.save()
                return HttpResponse("<script>alert('driver logged');window.location='/accounts/driverhome/';</script>")
                # return redirect('driverhome')  
            else:
            #    messages.success(request,'Access Denied!!!')
               return HttpResponse("<script>alert('driver not logged');window.location='/accounts/drlog/';</script>")
            #    return redirect('drlog')    
        else:
            return HttpResponse("<script>alert('it is not a driver');window.location='/accounts/drlog/';</script>")
            # messages.success(request, 'Access Denied!!!')
            return redirect('drlog') 
    ann=Account.objects.filter(is_driver=True) 
    er=Account.objects.filter()        
    return render(request,'drlog.html',{'ann':ann}) 

# def Driverlog(request):
 
#     if request.method == 'POST':
#         user=request.user
#         print(user)
#         phone_number = request.POST['phone_number']
#         print(phone_number)
#         if(Account.objects.filter(phone=phone_number)):
#             log=Account.objects.filter(phone=phone_number).values('role').get()['role']
#             print(log)
#             if log == 'is_driver':
#                 otp = str(randint(100000, 999999))
#                 message = f'Your OTP is {otp}. Do not share it with anyone.'
#                 try:
#                     # replace with your Twilio phone number and sender ID
#                     client.messages.create(to=phone_number, from_='+15155828771', body=message)
#                     return JsonResponse({'status': 'success', 'message': 'OTP sent successfully.'})
#                 except:
#                     return JsonResponse({'status': 'error', 'message': 'Failed to send OTP. Please try again later.'})
            
#                 # return HttpResponse("<script>alert('OTP send');</script>")
                 
#             else: 
#                return HttpResponse("<script>alert('driver not logged');window.location='/accounts/drlog/';</script>")  
#         else:
#             return HttpResponse("<script>alert('it is not a driver');window.location='/accounts/drlog/';</script>")
            
#     ann=Account.objects.filter(is_driver=True) 
#     er=Account.objects.filter()        
#     return render(request,'drlog.html',{'ann':ann}) 


def Driverotp(request):
    return render(request,'drotp.html')

def AdminLocation(request):
    return render(request,'adminlocations.html')



ENDPOINT ="https://api.postalpincode.in/pincode/"

def pincode_view(request):
    if request.method == 'POST':
        pickup_pincode = request.POST.get('pickup_pincode')
        # delivery_pincode = request.POST.get('delivery_pincode')
        print(pickup_pincode)

        pin_start = str(670001)
        pin_end = str(695615)

        if (pickup_pincode >= pin_start and pickup_pincode <= pin_end) :
        # and (delivery_pincode >= pin_start and delivery_pincode <= pin_end): 

            pickup_response = requests.get(ENDPOINT + pickup_pincode )
            pickup_pincode_information = json.loads(pickup_response.text)
            pickup_information = pickup_pincode_information[0]['PostOffice'][0]
            print(pickup_information)
            
            # delivery_response = requests.get(ENDPOINT + delivery_pincode )
            # delivery_pincode_information = json.loads(delivery_response.text)
            # delivery_information = delivery_pincode_information[0]['PostOffice'][0]

            return render(request, 'pin.html', {
                'pickup_information': pickup_information,
                # 'delivery_information': delivery_information,
            })
        else:
            print(1)
            return render(request, 'pin.html', {'error': 'Pincode not valid. Enter a pincode existing in Kerala.'})

    return render(request, 'pin.html')
   
        


    
