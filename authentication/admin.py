from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    change_password_form = AdminPasswordChangeForm

    fieldsets = (
        ('Personal info', {'fields': ('email', 'first_name', 'last_name','phone')}),
        ('Password', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role', 'groups', 'user_permissions')}),
    )

    # Customize add fieldsets
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, CustomUserAdmin)
