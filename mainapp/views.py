from django.shortcuts import render

from datetime import date
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Register
from administrator.models import ApprovedUsers
from django.contrib.auth.models import User
from administrator.user import password,Remail
# Create your views here.
def index(request):
    return render(request,'home.html')




def register(request):
    if request.method=='GET':
        messages.warning(request, 'Must Allow Your Location')
        return render(request,'register.html')
    elif request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('email')
        contact=request.POST.get('cnum')
        whatsapp=request.POST.get('wnum')
        role=request.POST.get('role')
        lat=str(request.POST.get('lat'))
        long=str(request.POST.get('long'))
        

        try:
            if(Register.objects.exists()):
                c=Register.objects.count()
                record=Register(first_name=fname,last_name=lname,email=mail,contact_no=contact,whatsapp_no=whatsapp,role=role,created_at=date.today(),number=c+1,latitude=lat,longitude=long)
                record.save()
            else:
                record=Register(first_name=fname,last_name=lname,email=mail,contact_no=contact,whatsapp_no=whatsapp,role=role,created_at=date.today(),number=1,latitude=lat,longitude=long)
                record.save()
            messages.success(request, 'Successfully Registered!')
        except:
            messages.error(request, 'Something went wrong!!!')

        return render(request,'register.html')



def loginn(request):
    if request.method=='GET':
       if request.user.is_authenticated:
            return redirect('home')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.warning(request, 'Wrong Username or Password')

        return render(request,'login.html')
    return render(request,'login.html')    


def recover(request):
    if request.method=='GET':
        return render(request,'forgetpassword.html')
    elif request.method=='POST':
        userid=request.POST.get('username')
        email=request.POST.get('email')
     
        if userid and email:
            obj=ApprovedUsers.objects.filter(userid=userid)
            obj2=User.objects.get(username=userid)


            name=obj.values('first_name')[0]['first_name'] +' '+obj.values('last_name')[0]['last_name']
            prev_email=obj.values('email')[0]['email']
            Password=password()
            if prev_email==email:
                try:
                    obj2.set_password(Password)
                    obj2.save()
                    Remail(email,name,Password)
                    messages.success(request,'Check Your Email!')
                except:
                    messages.error(request,'Recovery Failed!')
            else:
                messages.error(request,'Enter correct Email!')
        return render(request,'forgetpassword.html')
    else:
        return render(request,'forgetpassword.html')



def logoutt(request):
    logout(request)
    return redirect('home')
