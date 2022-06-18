from datetime import datetime
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from manufacturer.models import CreatedProducts, Distribute,SetProduct
from administrator.models import ApprovedUsers
from .models import DistributeToRetailer,Stock
# Create your views here.

@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'distributor/distribute.html')
    elif request.method=='POST':
        product=request.POST.get('pro')
        retailer=request.POST.get('users')
        number=request.POST.get('number')

        my_obj=ApprovedUsers.objects.filter(userid=retailer)
        retailer_name=my_obj.values('first_name')[0]['first_name']+' '+my_obj.values('last_name')[0]['last_name']
       
        an_obj=CreatedProducts.objects.filter(name=product)
        product_id=an_obj.values('Product_id')[0]['Product_id']
        total_price=str(int(an_obj.values('price')[0]['price'])*int(number))


        if product and retailer and number:
         

           r_stock=Stock.objects.filter(distributor=request.user.username)
           stock=r_stock.filter(product_name=product)
           pre_stock=stock.values('total')[0]['total']
           remain_stock=int(int(pre_stock)-int(number))

           obj=DistributeToRetailer.objects.filter(Retailer_id=retailer)
           r_obj=obj.filter(distributor_id=request.user.username)
           re_obj=r_obj.filter(product_name=product)
           if not re_obj.exists():
             if remain_stock>0:
                try:
                    x=DistributeToRetailer(Retailer_id=retailer,Retailer_username=retailer_name,product_id=product_id,product_name=product,product_quantity=number,total_price=total_price,distributor_id=request.user.username,date=datetime.today())
                    x.save()
                    
                    stock.update(total=remain_stock)
                    messages.success(request, f'{product} is successfully distributed to {retailer}!')
                except:
           
                    messages.error(request, 'Something went wrong!!!')
       
             else:
                messages.error(request, f'Stock for {product} is not enough!!!')
       
       
           else:
              if remain_stock>0:
                re_obj.update(product_quantity=number)
                re_obj.update(total_price=total_price)
                stock.update(total=remain_stock)
                messages.success(request, f'{product} quantity has been changed!')

              else:
                messages.error(request, f'Stock for {product} is not enough!!!')


        return render(request,'distributor/distribute.html')

    return render(request,'distributor/distribute.html')


@login_required(login_url='http://127.0.0.1:8000/login/')
def retailerChanel(request):
    return render(request,'distributor/retailerChanel.html')




@login_required(login_url='http://127.0.0.1:8000/login/')
def products(request):
    if request.method=='GET':
          
        listt=[]
        total=0
        a=set()
        
        obj=Distribute.objects.filter(user=request.user.username)
        if obj.exists():
            for i in range(0,obj.count()):
               listt.append(obj.values('product_name')[i]['product_name'])
        
            dict_of_counts = {item:listt.count(item) for item in listt}
            for i in range(0,len(listt)):
                a.add(listt[i])


            for i in a:
                my_obj=Stock.objects.filter(product_name=i)
                myy_obj=Stock.objects.filter(distributor=request.user.username)
                if not (my_obj.exists() and myy_obj.exists()):
                    if(int(dict_of_counts[i])>1):
                        r_obj=obj.filter(product_name=i)
                        for j in range(0,r_obj.count()):
                            total+=int(r_obj.values('product_quantity')[j]['product_quantity'])

                        if(total!=0):    
                            obb=SetProduct.objects.filter(name=i)
                            x=Stock(distributor=request.user.username,product_id=r_obj.values('product_id')[0]['product_id'],product_name=i,product_price=str(int(r_obj.values('total_price')[0]['total_price'])/int(r_obj.values('product_quantity')[0]['product_quantity'])),product_desc=obb.values('description')[0]['description'],total=str(total))
                            x.save()
                    else:
                        r_obj=obj.filter(product_name=i)
                        q=r_obj.values('product_quantity')[0]['product_quantity']
                        obb=SetProduct.objects.filter(name=i)
                        x=Stock(distributor=request.user.username,product_id=r_obj.values('product_id')[0]['product_id'],product_name=i,product_price=str(int(r_obj.values('total_price')[0]['total_price'])/int(r_obj.values('product_quantity')[0]['product_quantity'])),product_desc=obb.values('description')[0]['description'],total=q)
                        x.save()
                  
                    
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
                    'date':obj.values('date')[i]['date'],
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



@api_view(['GET','POST'])
def gettotalproducts(request):
    if request.method=='GET':
            prod=[]
            obj=Stock.objects.filter(distributor=request.user.username)
            if obj.exists():
                for i in range(0,obj.count()):
                    data={
                        'id':obj.values('product_id')[i]['product_id'],
                        'name':obj.values('product_name')[i]['product_name'],
                        'price':obj.values('product_price')[i]['product_price'],
                        'desc':obj.values('product_desc')[i]['product_desc'],
                        'total':obj.values('total')[i]['total'],
                    }
                    prod.append(data)
            
            return Response(prod)

        
            
        
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})




@api_view(['GET','POST'])
def distributiondetails(request):
    if request.method=='GET':
        distributes=DistributeToRetailer.objects.filter(distributor_id=request.user.username)
        dist=[]
        if distributes.exists():
            for i in range(0,distributes.count()):
                data={
                    'id':distributes.values('Retailer_id')[i]['Retailer_id'],
                    'users':distributes.values('Retailer_username')[i]['Retailer_username'],
                    'product_id':distributes.values('product_id')[i]['product_id'],
                    'product_name':distributes.values('product_name')[i]['product_name'],
                    'product_quantity':distributes.values('product_quantity')[i]['product_quantity'],
                    'total_price':distributes.values('total_price')[i]['total_price']
                }
                dist.append(data)
       
        return Response(dist)
    elif request.method=='POST':
        msg=(request.data['msg'])
        if msg:
            obj=Distribute.objects.filter(distributor_id=request.user.username)
            obj.delete()
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})