from django.contrib import admin

from .models import ApprovedUsers,DeletedUser

admin.site.register(ApprovedUsers)
admin.site.register(DeletedUser)
