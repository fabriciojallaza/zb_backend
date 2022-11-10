from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _  # For text translations

from core import models


# Register custom User model
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email']
    fieldsets = ((None, {'fields': ('username', 'email', 'password')}),
                 (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}))
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2'), }),)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Product)
