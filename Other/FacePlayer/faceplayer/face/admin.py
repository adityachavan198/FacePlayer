from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'created_at','first_name','last_name','email']
    search_fields=['id','first_name','last_name','email']

admin.site.register(UserOfApp,UserAdmin)
