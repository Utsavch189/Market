from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from manufacturer.models import Distribute,SetProduct
from administrator.models import ApprovedUsers
from .models import DistributeToRetailer
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    return render(request,'distributor/distribute.html')


@login_required(login_url='http://127.0.0.1:8000/login/')
def products(request):
    if request.method=='GET':
        return render(request,'distributor/products.html')
    elif request.method=='POST':
        return render(request,'distributor/products.html')
    return render(request,'distributor/products.html')




@api_view(['GET','POST'])
def getproducts(request):
    if request.method=='GET':
        prod=[]
        obj=Distribute.objects.filter(user=request.user.username)
        if obj.exists():
            for i in range(0,obj.count()):
                p=SetProduct.objects.filter(name=obj.values('product_name')[i]['product_name'])
                m=ApprovedUsers.objects.filter(userid=obj.values('manufacturer_id')[i]['manufacturer_id'])
                
                data={
                    'p_id':obj.values('product_id')[i]['product_id'],
                    'p_name':obj.values('product_name')[i]['product_name'],
                    'p_price':str(int(obj.values('total_price')[i]['total_price'])/int(obj.values('product_quantity')[i]['product_quantity'])),
                    'p_desc':p.values('description')[0]['description'],
                    'p_in_stock':obj.values('product_quantity')[i]['product_quantity'],
                    'distributor':m.values('first_name')[0]['first_name']+' '+m.values('last_name')[0]['last_name'],
                }
        
                prod.append(data)
            return Response(prod)
        else:
            return Response({'info':'no data'})
        
            
        
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})


@api_view(['GET','POST'])
def getretailers(request):
    if request.method=='GET':
        retail=[]
        obj=ApprovedUsers.objects.filter(role='Retailer')
        if obj.exists():
            for i in range(0,obj.count()):
              
                
                data={
                    'userid':obj.values('userid')[i]['userid'],
                    'username':obj.values('first_name')[i]['first_name']+' '+obj.values('last_name')[i]['last_name'],
                    'email':obj.values('email')[0]['email'],
                    'conatact':obj.values('contact_no')[0]['contact_no'],
                    'whatsapp':obj.values('whatsapp_no')[i]['whatsapp_no'],
                   
                }
        
                retail.append(data)
            return Response(retail)
        else:
            return Response({'info':'no data'})
        
            
        
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})