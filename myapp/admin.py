from django.contrib import admin
from myapp.models import customer

# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display=('name', 'phone', 'email', 'address', 'message', 'itemAmount')

admin.site.register(customer, customerAdmin)
