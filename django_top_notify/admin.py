from django.contrib import admin
from . import models


@admin.register(models.SystemTopNotification)
class SystemTopNotificationAdmin(admin.ModelAdmin):
    list_display = ["id", "publish_time", "expired", "content"]
    search_fields = ["content"]
