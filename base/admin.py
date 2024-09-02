from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Customize the admin fields for the CustomUser model
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('department', 'role')}),
    )

# Register the CustomUser model with the customized admin settings
admin.site.register(CustomUser, CustomUserAdmin)

# Remove or comment out the line below as Group is already registered by Django
# admin.site.register(Group)
