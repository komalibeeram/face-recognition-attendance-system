from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('username', 'enroll_id', 'date_joined', 'last_login', 'is_student', 'is_active','is_admin')
    search_fields = ('enroll_id', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)