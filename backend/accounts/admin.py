from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_staff')
    search_fields = ('email', 'full_name')
    list_filter = ('role', 'is_staff')
    ordering = ('email',)

# Register the model with the customized Admin view
admin.site.register(User, UserAdmin)

