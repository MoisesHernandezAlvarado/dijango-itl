from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('id', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)  
    
# Register your models here.
admin.site.register(User, UserAdmin)