from django.contrib import admin
from myapp.models import product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display=('pname', 'pprice', 'pimage', 'pdescription', 'pstock')

admin.site.register(product, )
