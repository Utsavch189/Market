from datetime import date
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from administrator.models import ApprovedUsers
from .models import CreatedProducts,SetProduct,Distribute
from .product_id import Product


@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'manufacturer/production.html')
    elif request.method=='POST':
        product=request.POST.get('pro')
        number=request.POST.get('number')
        if product and number:
             try:
                obj=SetProduct.objects.filter(name=product)
                
                if obj.exists():
                    r_obj=CreatedProducts.objects.filter(name=product)
                    if not r_obj.exists():
                        price=obj.values('price')[0]['price']
                        desc=obj.values('description')[0]['description']
                        newproduct=CreatedProducts(Product_id=Product(product),name=product,price=price,description=desc,production_no=number,production_date=date.today())
                        newproduct.save()
                        messages.success(request, f'Successfully Create the first entry for {product} and entered production number')
                    else:
                        price=obj.values('price')[0]['price']
                        desc=obj.values('description')[0]['description']
                        r_obj.update(price=price,description=desc,production_no=number)
                        messages.success(request, f'Successfully Update the Production number for {product}')

             except:
                 messages.error(request, 'Something went wrong!!!')
        else:
            messages.error(request, 'Number of Products OR Product name is missing')


        return render(request,'manufacturer/production.html')
    else:
        return render(request,'manufacturer/production.html')






@login_required(login_url='http://127.0.0.1:8000/login/')
def setproducts(request):
    if request.method=='GET':
        
        return render(request,'manufacturer/setproducts.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        if name and price and desc: 
            my_obj=SetProduct.objects.filter(name=name)
            if not my_obj.exists():
                try:
                    product=SetProduct(name=name,price=price,description=desc)
                    product.save()
                    messages.success(request, f'{name} is Successfully Added!')
                except:
                    messages.error(request, 'Something went wrong!!!')
            else:
                
                my_obj.update(name=name,price=price,description=desc)
        val=request.POST.get('pro')
        if val:
            try:
                obj=SetProduct.objects.filter(name=val)
                obj.delete()
                messages.success(request, f'{val} is Successfully Removed!')
            except:
                messages.error(request, 'Something went wrong!!!')
        return render(request,'manufacturer/setproducts.html')
    return render(request,'manufacturer/setproducts.html')





@login_required(login_url='http://127.0.0.1:8000/login/')
def distribution(request):
    if request.method=='GET':
        return render(request,'manufacturer/distribution.html')
    elif request.method=='POST':
        product=request.POST.get('pro')
        user=request.POST.get('users')
        number=request.POST.get('number')
        manufacturer=(request.user.first_name)
        if product and user and number:
            prod=CreatedProducts.objects.filter(name=product)
            prod_id=prod.values('Product_id')[0]['Product_id']
            price=int(prod.values('price')[0]['price'])
            obj=Distribute.objects.filter(user=user)
            r_obj=obj.filter(product_name=product)
            an_obj=Distribute.objects.filter(take_from=manufacturer)
            my_obj=ApprovedUsers.objects.filter(userid=user)
            take_from=obj.filter(take_from=manufacturer)
            username=my_obj.values('first_name')[0]['first_name']+' '+my_obj.values('last_name')[0]['last_name']
            try:
                if not (obj.exists() and r_obj.exists() and an_obj.exists()):
                
                
                    x=Distribute(user=user,product_id=prod_id,take_from=request.user.first_name,product_name=product,product_quantity=number,total_price=str(price*int(number)),date=date.today())
                    x.save()
                    messages.success(request, f'{product} is successfully distributed to {username}!')
                  
                else:
              
                    r_obj.update(product_quantity=number,total_price=str(price*int(number)),date=date.today())
                    messages.success(request, f'{product} has been successfully updated for {username}!')
            except:
                messages.error(request, 'Something went wrong!!!')

        else:
            pass
        return render(request,'manufacturer/distribution.html')
    return render(request,'manufacturer/distribution.html')













@api_view(['GET','POST'])
def setproduct(request):
    if request.method=='GET':
        
            prod=[]
            alls=SetProduct.objects.all()
            
            if alls.exists():
                    for i in range(0,alls.count()):
                        data={
                            
                            'name':alls.values('name')[i]['name'],
                            'price':alls.values('price')[i]['price'],
                            'desc':alls.values('description')[i]['description'],
                           
                        }
                        prod.append(data)
                    return Response(prod)
            return Response({'info':'no data'})
            
        
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})



@api_view(['GET','POST'])
def manufacturedproducts(request):
    if request.method=='GET':
        
            prod=[]
            alls=CreatedProducts.objects.all()
            
            if alls.exists():
                    for i in range(0,alls.count()):
                        data={
                            'id':alls.values('Product_id')[i]['Product_id'],
                            'name':alls.values('name')[i]['name'],
                            'price':alls.values('price')[i]['price'],
                            'desc':alls.values('description')[i]['description'],
                            'number':alls.values('production_no')[i]['production_no'],
                           
                        }
                        prod.append(data)
                    return Response(prod)
            return Response({'info':'no data'})
            
        
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})


@api_view(['GET','POST'])
def distribute(request):
    if request.method=='GET':
        distributor=ApprovedUsers.objects.filter(role='Distributor')
        if distributor.exists():
            distributors=[]
            for i in range(0,distributor.count()):
                data={
                    'userid':distributor.values('userid')[i]['userid'],
                    'name':(distributor.values('first_name')[i]['first_name'])+' '+(distributor.values('last_name')[0]['last_name']),
                    'contact':distributor.values('contact_no')[i]['contact_no'],
                    'whatsapp':distributor.values('whatsapp_no')[i]['whatsapp_no'],
                    'email':distributor.values('email')[i]['email'],
                }
                distributors.append(data)
        return Response(distributors)
    elif request.method=='POST':
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})
