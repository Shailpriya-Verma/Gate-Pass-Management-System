from django.contrib import admin
from .models import *

# Register your models here.

class registrationAdmin(admin.ModelAdmin):
    list_display=('name','rid','passwd','course','address','pic','ryear','mob','email')
admin.site.register(registration,registrationAdmin)

class guardregistrationAdmin(admin.ModelAdmin):
    list_display=('name','guardid','passwd','address','pic','mob','email','rdate')
admin.site.register(guardregistration,guardregistrationAdmin)

class adminloginAdmin(admin.ModelAdmin):
    list_display=('userid','passwd')
admin.site.register(adminlogin,adminloginAdmin)

class requestpassAdmin(admin.ModelAdmin):
    list_display=('id','regid','fromdate','fromtime','todate','totime','reqtime','reason','status','adminremark','permitstatus','permittime')
admin.site.register(requestpass,requestpassAdmin)