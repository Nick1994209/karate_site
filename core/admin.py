from django.contrib import admin

# Register your models here.

from core.models import User #, GroupUsers


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

# class GroupUsersAdmin(admin.ModelAdmin):
#     list_display = ('name', 'text',)
#     list_filter = ('name', 'text')

admin.site.register(User, UserAdmin)
# admin.site.register(GroupUsers, GroupUsersAdmin)