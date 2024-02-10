from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('ci',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('ci',)}),
    )
    list_display = ("username", "last_login", "first_name", "last_name", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
