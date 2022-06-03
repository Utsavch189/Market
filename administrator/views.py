from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from mainapp.models import Register
import json
# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
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
