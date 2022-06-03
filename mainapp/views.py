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
# Create your views here.
def index(request):
    return render(request,'home.html')




def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('email')
        contact=request.POST.get('cnum')
        whatsapp=request.POST.get('wnum')
        role=request.POST.get('role')

        try:
            if(Register.objects.exists()):
                c=Register.objects.count()
                record=Register(first_name=fname,last_name=lname,email=mail,contact_no=contact,whatsapp_no=whatsapp,role=role,created_at=date.today(),number=c+1)
                record.save()
            else:
                record=Register(first_name=fname,last_name=lname,email=mail,contact_no=contact,whatsapp_no=whatsapp,role=role,created_at=date.today(),number=1)
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



def logoutt(request):
    logout(request)
    return redirect('home')
