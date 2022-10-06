from django.contrib import admin
from myapp.models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('username')

admin.site.register(User)
