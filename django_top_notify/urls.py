from django.conf.urls import url

from . import views

app_name = "django_top_notify"

urlpatterns = [
    url(r"^latest_system_notification/$", views.get_latest_system_notification, name="latest_system_notification"),
]
