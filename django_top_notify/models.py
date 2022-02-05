from django.db import models

from . import constants


class SystemTopNotification(models.Model):
    content = models.TextField(help_text="System notification content")
    expired = models.BooleanField(default=False, help_text="Is the notification expired")
    publish_time = models.DateTimeField(auto_now=True, help_text="Time of publishing the notification")
    category = models.CharField(choices=constants.TOP_NOTIFY_CATEGORIES, max_length=128,
                                help_text="Category of the notification")
