from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from mainapp.models import Register
import json
from .models import ApprovedUsers
from django.contrib.auth.models import User
from .user import mail,password,useID




@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'administrator/index.html')
    elif request.method=='POST':
        val=request.POST.get('role')
        approved=request.POST.get('approved')
     
        obj=Register.objects.filter(number=str(val))
        obj.delete()
        if approved!=None:
            r_obj=Register.objects.filter(number=str(approved))
            if r_obj.exists():
                
                Password=password()
                name=str( r_obj.values('first_name')[0]['first_name'])+' '+str(r_obj.values('last_name')[0]['last_name'])
                email=r_obj.values('email')[0]['email']
                userid=useID(r_obj.values('first_name')[0]['first_name'])
              

                
                try:
                    mail(email,name,r_obj.values('role')[0]['role'],userid,Password)
                    user=User.objects.create_user(userid, email, Password)
                    user.first_name =name
                    user.last_name = r_obj.values('role')[0]['role']
                    user.email = email
                    user.save()
                    approvedUser=ApprovedUsers(author=user,userid=userid,first_name=r_obj.values('first_name')[0]['first_name'],last_name=r_obj.values('last_name')[0]['last_name'],email=r_obj.values('email')[0]['email'],contact_no=r_obj.values('contact_no')[0]['contact_no'],whatsapp_no=r_obj.values('whatsapp_no')[0]['whatsapp_no'],role=r_obj.values('role')[0]['role'])
                    approvedUser.save()
                    r_obj.delete()
                    messages.success(request, 'Successfully Approved!')
                except:
                    messages.error(request, 'Something went wrong!!!')
        
        return render(request,'administrator/index.html')
    return render(request,'administrator/index.html')


@api_view(['GET','POST'])
def pending(request):
    if request.method=='GET':
        users=[]
        alls=Register.objects.all()

        

        for i in range(0,alls.count()):
            data={
                'number':alls.values('number')[i]['number'],
                'name':alls.values('first_name')[i]['first_name']+' '+alls.values('last_name')[i]['last_name'],
                'email':alls.values('email')[i]['email'],
                'contact':alls.values('contact_no')[i]['contact_no'],
                'whatsapp':alls.values('whatsapp_no')[i]['whatsapp_no'],
                'role':alls.values('role')[i]['role']
            }

        
       
            users.append(data)
        return Response(users)
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})
