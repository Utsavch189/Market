from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from mainapp.models import Register
import json
from .models import ApprovedUsers,SetProduct
from django.contrib.auth.models import User
from .user import mail,password,useID




@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'administrator/pending.html')
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
        if obj.exists():
            obj.delete()
            messages.success(request, 'Successfully Removed!')
        return render(request,'administrator/approve.html')

    else:
        return render(request,'administrator/approve.html')









@login_required(login_url='http://127.0.0.1:8000/login/')
def setproducts(request):
    if request.method=='GET':
        
        return render(request,'administrator/setproducts.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        if name and price and desc: 
            try:
                product=SetProduct(name=name,price=price,description=desc)
                product.save()
                messages.success(request, f'{name} is Successfully Added!')
            except:
                messages.error(request, 'Something went wrong!!!')

        val=request.POST.get('pro')
        if val:
            try:
                obj=SetProduct.objects.filter(name=val)
                obj.delete()
                messages.success(request, f'{val} is Successfully Deleted!')
            except:
                messages.error(request, 'Something went wrong!!!')
        return render(request,'administrator/setproducts.html')
    return render(request,'administrator/setproducts.html')






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
            if(request.user.last_name=='Admin'):
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
        return Response({'info':'You have no permission!'})
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})




@api_view(['GET','POST'])
def setproduct(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            approveUsers=[]
            alls=SetProduct.objects.all()
            if(request.user.last_name=='Admin'):
                if alls.exists():
                    for i in range(0,alls.count()):
                        data={
                            
                            'name':alls.values('name')[i]['name'],
                            'price':alls.values('price')[i]['price'],
                            'desc':alls.values('description')[i]['description'],
                           
                        }
                        approveUsers.append(data)
                    return Response(approveUsers)
                return Response({'info':'no data'})
            return Response({'info':'You have no permission!'})
        return Response({'info':'You have no permission!'})
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})
