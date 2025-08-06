# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Optionally, customize the UserAdmin here, for example adding fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Unregister the original User admin
admin.site.unregister(User)
# Register the User model with your customized admin
admin.site.register(User, CustomUserAdmin)
