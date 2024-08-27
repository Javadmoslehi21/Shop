from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "full_name", "is_staff", "is_active",)
    search_fields = ("email", "full_name",)
    ordering = ("email",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ('Authentication', {
            "fields": ('email', 'password', "full_name",
                       ),
        }),
        ('Permissions', {
            "fields": ('is_staff', 'is_active', 'is_superuser', 'is_teacher',
                       ),
        }),
        ('Group Permissions', {
            "fields": ('groups', 'user_permissions',
                       ),
        }),
        ('Important Date', {
            "fields": ('last_login',
                       ),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                "email", "full_name", "password1", "password2", "is_staff",
                "is_active", 'is_superuser', 'is_teacher'
            )}
         ),
    )


admin.site.register(User, UserAdmin)
