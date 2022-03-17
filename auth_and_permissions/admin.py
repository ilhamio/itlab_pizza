from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
from auth_and_permissions.models import Staff, User


class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'Работники'


class UserAdmin(BaseUserAdmin):
    inlines = (StaffInline,)


admin.site.register(User, UserAdmin)
