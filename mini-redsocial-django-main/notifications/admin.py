from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sender', 'notification_type', 'created_at')
    search_fields = ('user__id', 'sender__id', 'notification_type')
    list_filter = ('notification_type', 'created_at')
