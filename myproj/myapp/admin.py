from django.contrib import admin
from myapp.models import katalog
# Register your models here.

class newprod(admin.ModelAdmin):
    list_display = ['phone','cost','gb','camer']

admin.site.register(katalog,newprod)