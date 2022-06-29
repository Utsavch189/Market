from datetime import date
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from mainapp.models import Register
from .models import ApprovedUsers,DeletedUser
from django.contrib.auth.models import User
from .user import mail,password,useID




@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'administrator/pending.html')
    elif request.method=='POST':
        val=request.POST.get('role')
        approved=request.POST.get('approved')
     
        obj=Register.objects.filter(number=(val))
        obj.delete()
        if approved!=None:
            r_obj=Register.objects.filter(number=(approved))
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
                    approvedUser=ApprovedUsers(author=user,userid=userid,first_name=r_obj.values('first_name')[0]['first_name'],last_name=r_obj.values('last_name')[0]['last_name'],email=r_obj.values('email')[0]['email'],contact_no=r_obj.values('contact_no')[0]['contact_no'],whatsapp_no=r_obj.values('whatsapp_no')[0]['whatsapp_no'],role=r_obj.values('role')[0]['role'],latitude=r_obj.values('latitude')[0]['latitude'],longitude=r_obj.values('longitude')[0]['longitude'])
                    approvedUser.save()
                    r_obj.delete()
                    messages.success(request, f'{name} is Successfully Approved!')
                except:
                    messages.error(request, 'Something went wrong!!!')
        
        return render(request,'administrator/pending.html')
    return render(request,'administrator/pending.html')





@login_required(login_url='http://127.0.0.1:8000/login/')
def approved(request):
    if request.method=='GET':
        dict={
            'manufacturer':ApprovedUsers.objects.filter(role='Manufacturer').count(),
            'distributor':ApprovedUsers.objects.filter(role='Distributor').count(),
            'retailer':ApprovedUsers.objects.filter(role='Retailer').count(),
        }
        return render(request,'administrator/approve.html',{'dict':dict})

    elif request.method=='POST':
        val=request.POST.get('role')

        obj=User.objects.filter(username=val)
        my_obj=ApprovedUsers.objects.filter(userid=val)

        first_name=my_obj.values('first_name')[0]['first_name']
        last_name=my_obj.values('last_name')[0]['last_name']
        email=my_obj.values('email')[0]['email']
        contact_no=my_obj.values('contact_no')[0]['contact_no']
        whatsapp_no=my_obj.values('whatsapp_no')[0]['whatsapp_no']
        role=my_obj.values('role')[0]['role']

        if obj.exists():
            try:
                x=DeletedUser(first_name=first_name,last_name=last_name,email=email,contact_no=contact_no,whatsapp_no=whatsapp_no,role=role,date=date.today())
                x.save()
                obj.delete()
                messages.success(request, 'Successfully Removed!')
            except:
                messages.error(request, 'Does not Removed Successfully!')
        return render(request,'administrator/approve.html')

    else:
        return render(request,'administrator/approve.html')





@login_required(login_url='http://127.0.0.1:8000/login/')
def delteduser(request):
    if request.method=='GET':
        return render(request,'administrator/deleteduser.html')
    elif request.method=='POST':
        return render(request,'administrator/deleteduser.html')
    else:
        return render(request,'administrator/deleteduser.html')








@api_view(['GET','POST'])
def pending(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            users=[]
            alls=Register.objects.all()
            if(request.user.last_name=='Admin'):
        
                if alls.exists():
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
                return Response({'info':'no data'})
            return Response({'info':'You have no permission!'})
        return Response({'info':'You have no permission!'})
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})






@api_view(['GET','POST'])
def approve(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            approveUsers=[]
            alls=ApprovedUsers.objects.all()
            
            if alls.exists():
                    for i in range(0,alls.count()):
                        data={
                            'userid':alls.values('userid')[i]['userid'],
                            'name':alls.values('first_name')[i]['first_name']+' '+alls.values('last_name')[i]['last_name'],
                            'email':alls.values('email')[i]['email'],
                            'contact':alls.values('contact_no')[i]['contact_no'],
                            'whatsapp':alls.values('whatsapp_no')[i]['whatsapp_no'],
                            'role':alls.values('role')[i]['role']
                        }
                        approveUsers.append(data)
                    return Response(approveUsers)
            return Response({'info':'no data'})
            
        return Response({'info':'You have no permission!'})
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})



@api_view(['GET','POST'])
def deleted(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            approveUsers=[]
            alls=DeletedUser.objects.all()
            
            if alls.exists():
                    for i in range(0,alls.count()):
                        data={
                            'name':alls.values('first_name')[i]['first_name']+' '+alls.values('last_name')[i]['last_name'],
                            'email':alls.values('email')[i]['email'],
                            'contact':alls.values('contact_no')[i]['contact_no'],
                            'whatsapp':alls.values('whatsapp_no')[i]['whatsapp_no'],
                            'role':alls.values('role')[i]['role']
                        }
                        approveUsers.append(data)
                    return Response(approveUsers)
            return Response({'info':'no data'})
            
        return Response({'info':'You have no permission!'})
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})
