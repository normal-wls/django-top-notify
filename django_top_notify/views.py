from django.http import JsonResponse

from .models import SystemTopNotification


def get_latest_system_notification(request):
    notification = SystemTopNotification.objects.filter(expired=False).order_by("-publish_time").first()
    response = {}
    if notification:
        response = {
            "content": notification.content,
            "publish_time": notification.publish_time,
            "category": notification.category
        }
    return JsonResponse(response)
