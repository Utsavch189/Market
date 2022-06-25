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
        
        obb=Register.objects.filter(email=mail)
        if not obb.exists():
            if lat and long:
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
            else:
                messages.error(request, 'Allow Your location must!!!')
        else:
            messages.error(request, 'Already this email is taken!!!')
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
        
        email=request.POST.get('email')
     
        if  email:
            my_obj=ApprovedUsers.objects.filter(email=email)
            userid=my_obj.values('userid')[0]['userid']
            obj=ApprovedUsers.objects.filter(userid=userid)
            obj2=User.objects.get(username=userid)


            name=obj.values('first_name')[0]['first_name'] +' '+obj.values('last_name')[0]['last_name']
            prev_email=obj.values('email')[0]['email']
            Password=password()
            if prev_email==email:
                try:
                    obj2.set_password(Password)
                    obj2.save()
                    Remail(email,name,Password,userid)
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


@api_view(['GET','POST'])
def manufact(request):
    if request.method=='GET':
        obj=ApprovedUsers.objects.filter(role='Manufacturer')
        m=[]
        if obj.exists():
            for i in range(0,obj.count()):
                m.append(
                    [   float(obj.values('longitude')[i]['longitude']),
                        float(obj.values('latitude')[i]['latitude'])
                       
                    ]
                )

        return Response(m)
    elif request.method=='POST':
        return Response({'info':'running'})
    else:
        return Response({'info':'bad request'})



@api_view(['GET','POST'])
def distribut(request):
    if request.method=='GET':
        obj=ApprovedUsers.objects.filter(role='Distributor')
        m=[]
        if obj.exists():
            for i in range(0,obj.count()):
                m.append(
                    [   float(obj.values('longitude')[i]['longitude']),
                        float(obj.values('latitude')[i]['latitude'])
                        
                    ]
                )

        return Response(m)
    elif request.method=='POST':
        return Response({'info':'running'})
    else:
        return Response({'info':'bad request'})





@api_view(['GET','POST'])
def retailer(request):
    if request.method=='GET':
        obj=ApprovedUsers.objects.filter(role='Retailer')
        m=[]
        if obj.exists():
            for i in range(0,obj.count()):
                m.append(
                    [   float(obj.values('longitude')[i]['longitude']),
                        float(obj.values('latitude')[i]['latitude'])
                        
                    ]
                )

        return Response(m)
    elif request.method=='POST':
        return Response({'info':'running'})
    else:
        return Response({'info':'bad request'})


@api_view(['GET','POST'])
def allnetwork(request):
    if request.method=='GET':
        obj=ApprovedUsers.objects.filter(role='Manufacturer')
        obj1=ApprovedUsers.objects.filter(role='Retailer')
        obj2=ApprovedUsers.objects.filter(role='Distributor')
        m=[]
        n=[]
        res=[]
        if obj.exists():
            for i in range(0,obj.count()):
                m.append(
                    [   float(obj.values('longitude')[i]['longitude']),
                        float(obj.values('latitude')[i]['latitude'])
                        
                    ]
                
                )
                n.append(obj.values('userid')[i]['userid'])
        if obj1.exists():
            for i in range(0,obj1.count()):
                m.append(
                    [   float(obj1.values('longitude')[i]['longitude']),
                        float(obj1.values('latitude')[i]['latitude'])
                        
                    ]
                )
                n.append(obj1.values('userid')[i]['userid'])

        if obj2.exists():
            for i in range(0,obj2.count()):
                m.append(
                    [   float(obj2.values('longitude')[i]['longitude']),
                        float(obj2.values('latitude')[i]['latitude'])
                        
                    ]
                )
                n.append(obj2.values('userid')[i]['userid'])
        res.append(m)
        res.append(n)
        return Response(res)
    elif request.method=='POST':
        val=request.data['msg']
        
        obj=ApprovedUsers.objects.filter(userid=val)
        m=[]
        if obj.exists():
            for i in range(0,obj.count()):
                m.append(
                    [   float(obj.values('longitude')[i]['longitude']),
                        float(obj.values('latitude')[i]['latitude'])
                        
                    ]
                )

        return Response(m)
    else:
        return Response({'info':'bad request'})


@api_view(['GET','POST'])
def numbers(request):
    if request.method=='GET':
        obj=ApprovedUsers.objects.filter(role='Manufacturer')
        obj1=ApprovedUsers.objects.filter(role='Retailer')
        obj2=ApprovedUsers.objects.filter(role='Distributor')
        m=[
            {'manufa':obj.count()},
            {'distri':obj2.count()},
            {'retail':obj1.count()}
        ]


        return Response(m)
    elif request.method=='POST':
        return Response({'info':'running'})
    else:
        return Response({'info':'bad request'})

