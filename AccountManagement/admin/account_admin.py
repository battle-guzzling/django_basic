from django.contrib import admin
from AccountManagement.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "username", "email", "type")
    empty_value_display = "-empty-"