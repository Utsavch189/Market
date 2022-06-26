from datetime import date
from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from administrator.models import ApprovedUsers
from .models import CreatedProducts,SetProduct,Distribute,TotalProducts
from .product_iddd import Product
from mainapp.dates import dates


@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'manufacturer/production.html')
    elif request.method=='POST':
        product=request.POST.get('pro')
        number=request.POST.get('number')
        if product and number:
             try:
                main_obj=SetProduct.objects.filter(manufacturer_id=request.user.username)
                obj=main_obj.filter(name=product)

                if obj.exists():
                    ann_obj=CreatedProducts.objects.filter(manufacturer_id=request.user.username)
                    r_obj=ann_obj.filter(name=product)
                    if not r_obj.exists():
                        price=obj.values('price')[0]['price']
                        desc=obj.values('description')[0]['description']
                        
                        pro_id_get=CreatedProducts.objects.filter(name=product)
                        

                        if not pro_id_get.exists():
                            
                            newproduct=CreatedProducts(manufacturer_id=request.user.username,Product_id=Product(product),name=product,price=price,description=desc,production_no=number,production_date=date.today())
                            newproduct.save()
                            messages.success(request, f'Successfully Create the first entry for {product} and entered production number')
                        else:
                            pro_id=pro_id_get.values('Product_id')[0]['Product_id']
                            newproduct=CreatedProducts(manufacturer_id=request.user.username,Product_id=pro_id,name=product,price=price,description=desc,production_no=number,production_date=date.today())
                            newproduct.save()
                            messages.success(request, f'Successfully Create the first entry for {product} and entered production number')
                    else:
                        price=obj.values('price')[0]['price']
                        desc=obj.values('description')[0]['description']
                        production_no=r_obj.values('production_no')[0]['production_no']
                        val=str(int(production_no)+int(number))
                        r_obj.update(price=price,description=desc,production_no=val)
                        messages.success(request, f'Successfully Update the Production number for {product}')

             except:
                 messages.error(request, 'Something went wrong!!!')
        else:
            messages.error(request, 'Number of Products OR Product name is missing')


        return render(request,'manufacturer/production.html')
    else:
        return render(request,'manufacturer/production.html')


@login_required(login_url='http://127.0.0.1:8000/login/')
def distributorChannel(request):
    if request.method=='GET':
        return render(request,'manufacturer/distributorChannel.html')



@login_required(login_url='http://127.0.0.1:8000/login/')
def setproducts(request):
    if request.method=='GET':
        
        return render(request,'manufacturer/setproducts.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        
        if name and price and desc: 
            main_obj=SetProduct.objects.filter(manufacturer_id=request.user.username)
            my_obj=main_obj.filter(name=name)
            if not my_obj.exists():
                try:
                    product=SetProduct(manufacturer_id=request.user.username,name=name,price=price,description=desc)
                    product.save()
                    messages.success(request, f'{name} is Successfully Added!')
                except:
                    messages.error(request, 'Something went wrong!!!')
            else:
                
                my_obj.update(name=name,price=price,description=desc)
        val=request.POST.get('pro')
        if val:
            try:
                main_obj=SetProduct.objects.filter(manufacturer_id=request.user.username)
                obj=main_obj.filter(name=val)
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
        manufacturer=(request.user.username)
        if product and user and number:
            prod=CreatedProducts.objects.filter(name=product)
            prod_id=prod.values('Product_id')[0]['Product_id']
            price=int(prod.values('price')[0]['price'])
            
            obj=Distribute.objects.filter(user=user)
            an_obj=obj.filter(manufacturer_id=manufacturer)
            r_obj=an_obj.filter(product_name=product)

            ###
            t_obj=TotalProducts.objects.filter(manufacturer_id=manufacturer)
            rt_obj=t_obj.filter(product_name=product)
            ###

           
            my_obj=ApprovedUsers.objects.filter(userid=user)
            
            username=my_obj.values('first_name')[0]['first_name']+' '+my_obj.values('last_name')[0]['last_name']
            try:
                if not r_obj.exists()  :
                
                    ann_obj=CreatedProducts.objects.filter(manufacturer_id=request.user.username)
                    rr_obj=ann_obj.filter(name=product)
                    pre_stock=rr_obj.values('production_no')[0]['production_no']
                    remain_stock=str(int(pre_stock)-int(number))
                    if int(remain_stock)>=0:
                        x=Distribute(user=user,username=username,product_id=prod_id,manufacturer_id=manufacturer,product_name=product,product_quantity=number,total_price=str(price*int(number)),calculation_status=False,date=date.today())
                        x.save()
                        rr_obj.update(production_no=remain_stock)
                        ###
                        if not rt_obj.exists():
                            y=TotalProducts(product_id=prod_id,manufacturer_id=manufacturer,product_name=product,product_quantity=number,date=date.today())
                            y.save()
                        else:
                            val1=rt_obj.values('product_quantity')[0]['product_quantity']
                            new1_total=int(val1)+int(number)
                            rt_obj.update(product_quantity=str(new1_total))
                        ###
                        messages.success(request, f'{product} is successfully distributed to {username}!')
                    else:
                        messages.error(request, 'Do not have enough stock!!!')
                
              




                else:

                    l_date=r_obj.values('date')[0]['date']
                    l1_date=rt_obj.values('date')[0]['date']

                    if r_obj.exists() and l_date!=dates(1) and rt_obj.exists() and l1_date!=dates(1):
                        ann_obj=CreatedProducts.objects.filter(manufacturer_id=request.user.username)
                        rr_obj=ann_obj.filter(name=product)
                        pre_stock=rr_obj.values('production_no')[0]['production_no']
                        remain_stock=str(int(pre_stock)-int(number))
                        if int(remain_stock)>=0:
                            x=Distribute(user=user,username=username,product_id=prod_id,manufacturer_id=manufacturer,product_name=product,product_quantity=number,total_price=str(price*int(number)),calculation_status=False,date=date.today())
                            x.save()
                            rr_obj.update(production_no=remain_stock)

                            ###
                            y=TotalProducts(product_id=prod_id,manufacturer_id=manufacturer,product_name=product,product_quantity=number,date=date.today())
                            y.save()
                            ###

                            messages.success(request, f'{product} is successfully distributed to {username}!')
                        else:
                            messages.error(request, 'Do not have enough stock!!!')
                    else:
                        ann_obj=CreatedProducts.objects.filter(manufacturer_id=request.user.username)
                        rr_obj=ann_obj.filter(name=product)
                        pre_stock=rr_obj.values('production_no')[0]['production_no']
                        remain_stock=str(int(pre_stock)-int(number))
                        val=r_obj.values('product_quantity')[0]['product_quantity']
                        new_total=int(val)+int(number)
                        ###
                        val1=rt_obj.values('product_quantity')[0]['product_quantity']
                        new1_total=int(val1)+int(number)
                        
                        ###
                        if int(remain_stock)>=0:
                            r_obj.update(product_quantity=str(new_total),total_price=str(price*int(new_total)))
                            ###
                            rt_obj.update(product_quantity=str(new1_total))
                            ###
                            messages.success(request, f'{product} has been successfully updated for {username}!')
                            rr_obj.update(production_no=remain_stock)
                        else:
                            messages.error(request, 'Do not have enough stock!!!')
            except:
                messages.error(request, 'Something went wrong!!!')


        return render(request,'manufacturer/distribution.html')
    return render(request,'manufacturer/distribution.html')













@api_view(['GET','POST'])
def setproduct(request):
    if request.method=='GET':
        
            prod=[]
            alls=SetProduct.objects.filter(manufacturer_id=request.user.username)
            
            
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
            alls=CreatedProducts.objects.filter(manufacturer_id=request.user.username)

            
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
                    'name':(distributor.values('first_name')[i]['first_name'])+' '+(distributor.values('last_name')[i]['last_name']),
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



@api_view(['GET','POST'])
def distributiondetails(request):
    if request.method=='GET':
        distributes=Distribute.objects.filter(manufacturer_id=request.user.username)
        dist=[]
        if distributes.exists():
            for i in range(0,distributes.count()):
                data={
                    'id':distributes.values('user')[i]['user'],
                    'users':distributes.values('username')[i]['username'],
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
            obj=Distribute.objects.filter(manufacturer_id=request.user.username)
            obj.delete()
        return Response({'info':'Running'})
    else:
        return Response({'msg':'bad request','status':400})





@api_view(['GET','POST'])
def bestproductmanu(request):
    if request.method=='GET':
            p_obj=TotalProducts.objects.filter(manufacturer_id=request.user.username)
            prods=[]
            res=[]
            quant=[]
            if p_obj.exists():
                obj=p_obj.filter(date=dates(1))
                for i in range(0,obj.count()):
                
                    prods.append(obj.values('product_name')[i]['product_name'])
            
              
                for item in prods:
                    n_obj=obj.filter(product_name=item)
                    if n_obj.exists():
                        quant.append(n_obj.values('product_quantity')[0]['product_quantity'])

                res.append(prods)
                res.append(quant)

                return Response(res)
           
            else:
                return Response({'info':'no data'})
           

    elif request.method=='POST':
        val=request.data['value']
    
        if val==int(1) or val==int(2):
            p_obj=TotalProducts.objects.filter(manufacturer_id=request.user.username)
            prods=[]
            res=[]
            quant=[]
            if p_obj.exists():
                obj=p_obj.filter(date=dates(int(val)))
                for i in range(0,obj.count()):
                
                    prods.append(obj.values('product_name')[i]['product_name'])
            
              
                for item in prods:
                    n_obj=obj.filter(product_name=item)
                    if n_obj.exists():
                        quant.append(n_obj.values('product_quantity')[0]['product_quantity'])

                res.append(prods)
                res.append(quant)

                return Response(res)
           
            else:
                return Response({'info':'no data'})
        else:
            p_obj=TotalProducts.objects.filter(manufacturer_id=request.user.username)
            prods=set()
        
            res=[]
            quant=[]
        
            date=dates(3)
            for i in date:
                obj=p_obj.filter(date=i)
                if obj.exists():
                    for j in range(0,obj.count()):
                        prods.add(obj.values('product_name')[j]['product_name'])

            new_prods=list(prods)

            for item in new_prods:
                total=0
                c=p_obj.filter(product_name=item)
                if c.count()==1:
                    quant.append(int(c.values('product_quantity')[0]['product_quantity']))
                else:
                    for i in range(0,c.count()):
                        total+=int(c.values('product_quantity')[i]['product_quantity'])
                    quant.append(total)
            res.append(new_prods)
            res.append(quant)
            return Response(res)
        

        
    else:
        return Response({'info':'bad request'})