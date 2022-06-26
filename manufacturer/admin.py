from django.contrib import admin
from .models import CreatedProducts,SetProduct,Distribute,TotalProducts
# Register your models here.
admin.site.register(CreatedProducts)
admin.site.register(SetProduct)
admin.site.register(Distribute)
admin.site.register(TotalProducts)