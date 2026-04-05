from django.contrib import admin
from .models import User, Module, UserActivity, StudyResource, Notification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'stream')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'stream')

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'module', 'timestamp')

@admin.register(StudyResource)
class StudyResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'module_code', 'resource_type', 'uploaded_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read')
