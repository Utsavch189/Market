from django.contrib import messages
from numpy import number
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from administrator.models import ApprovedUsers
from distributor.models import DistributeToRetailer
from manufacturer.models import CreatedProducts,SetProduct
from .models import DistributeToCustomer,RetailerStock
from datetime import date




@login_required(login_url='http://127.0.0.1:8000/login/')
def stock(request):
    if request.method=='GET':
        pro=set()

        my_RetailerStock=RetailerStock.objects.filter(retailer=request.user.username)
        

        my_obj=DistributeToRetailer.objects.filter(Retailer_id=request.user.username)
        
        for i in range(0,my_obj.count()):
            pro.add(my_obj.values('product_id')[i]['product_id'])
           
        total=0
        total1=0
        listt=list(pro) 
        
        for i in listt:
            c0=my_obj.filter(product_id=i)
            c00=c0.filter(calculation_status=False)
            
            c=c00.count()
            
            obj=CreatedProducts.objects.filter(Product_id=i)
            pro_name=obj.values('name')[0]['name']
            pro_price=obj.values('price')[0]['price']
            pro_desc=obj.values('description')[0]['description']

            if c>1:
                
                for j in range(0,c):

                    m=(int(c00.values('product_quantity')[j]['product_quantity']))
                    total+=m
                    print(total)
                    
                    
                if not (my_RetailerStock.filter(product_id=i).exists()):
                    y=RetailerStock(retailer=request.user.username,product_id=i,product_name=pro_name,product_price=pro_price,product_desc=pro_desc,total=str(total))
                    y.save()
                else:
                    to=int(my_RetailerStock.filter(product_id=i).values('total')[0]['total'])
                    my_RetailerStock.filter(product_id=i).update(total=str(to+total))
                
                for j in range(0,c):
                    c0.update(calculation_status=True)
            elif c==1:
                total1+=int(c00.values('product_quantity')[0]['product_quantity'])
                if not (my_RetailerStock.filter(product_id=i).exists()):
                    y=RetailerStock(retailer=request.user.username,product_id=i,product_name=pro_name,product_price=pro_price,product_desc=pro_desc,total=str(total1))
                    y.save()
                else:
                    to=int(my_RetailerStock.filter(product_id=i).values('total')[0]['total'])
                    my_RetailerStock.filter(product_id=i).update(total=str(to+total1))
                c0.update(calculation_status=True)
            else:
                return render(request,'retailer/stock.html')

        return render(request,'retailer/stock.html')



@login_required(login_url='http://127.0.0.1:8000/login/')
def sell(request):
    if request.method=='GET':
        return render(request,'retailer/sell.html')
    elif request.method=='POST':
        product=request.POST.get('pro')
        number=request.POST.get('number')
        obj=DistributeToCustomer.objects.filter(Retailer_id=request.user.username)
        pro=obj.filter(product_name=product)

        
        if product and number:
            an_obj=CreatedProducts.objects.filter(name=product)
            product_id=an_obj.values('Product_id')[0]['Product_id']
            price=str(int(an_obj.values('price')[0]['price']))

            r_stock=RetailerStock.objects.filter(retailer=request.user.username)
            stock=r_stock.filter(product_name=product)
            pre_stock=stock.values('total')[0]['total']
            remain_stock=int(int(pre_stock)-int(number))
            if not pro.exists():
                if remain_stock>=0:
                 try:
                    x=DistributeToCustomer(Retailer_id=request.user.username,Retailer_username=str(request.user.first_name)+str(request.user.last_name),product_id=product_id,product_name=product,product_quantity=number,total_price=str(int(price)*int(number)),date=date.today())
                    x.save()
                    
                    stock.update(total=remain_stock)
                    messages.success(request, f'{product} is successfully selled !')
                 except:
           
                    messages.error(request, 'Something went wrong!!!')
                else:
                    messages.error(request, f'Stock for {product} is not enough!!!')
            else:
             if remain_stock>=0:
                val=pro.values('product_quantity')[0]['product_quantity']
                new_total=int(val)+int(number)
                pro.update(product_quantity=str(new_total))
                pro.update(total_price=str(new_total*int(price)))
                stock.update(total=remain_stock)
                messages.success(request, f'{product} quantity has been changed!')
        
             else:
                messages.error(request, f'Stock for {product} is not enough!!!')
        
        
        return render(request,'retailer/sell.html')
    else:
        return render(request,'retailer/sell.html')


@api_view(['GET','POST'])
def gettotalproducts(request):
    if request.method=='GET':
            prod=[]
            obj=RetailerStock.objects.filter(retailer=request.user.username)
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
        distributes=DistributeToCustomer.objects.filter(Retailer_id=request.user.username)
        dist=[]
        if distributes.exists():
            for i in range(0,distributes.count()):
                data={
                    
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
            obj=DistributeToRetailer.objects.filter(Retailer_id=request.user.username)
            obj.delete()
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})


@api_view(['GET','POST'])
def getproducts(request):
    if request.method=='GET':
        prod=[]
        obj=DistributeToRetailer.objects.filter(Retailer_id=request.user.username)
        if obj.exists():
            for i in range(0,obj.count()):
                p=SetProduct.objects.filter(name=obj.values('product_name')[i]['product_name'])
                m=ApprovedUsers.objects.filter(userid=obj.values('distributor_id')[i]['distributor_id'])
                
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