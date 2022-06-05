from django.contrib import messages
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from administrator.models import ApprovedUsers,SetProduct
from .models import CreatedProducts

@login_required(login_url='http://127.0.0.1:8000/login/')
def index(request):
    if request.method=='GET':
        return render(request,'manufacturer/production.html')
    elif request.method=='POST':
        return render(request,'manufacturer/production.html')
    else:
        return render(request,'manufacturer/production.html')



