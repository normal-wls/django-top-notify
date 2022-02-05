import json

from django.test import TestCase, Client
from django.urls import reverse

from django_top_notify.models import SystemTopNotification


class SystemNotificationTestCase(TestCase):
    def setUp(self):
        self.alert = SystemTopNotification(content="this is a alert notification", category="alert")
        self.alert.save()
        self.hint = SystemTopNotification(content="this is a hint notification", category="hint")
        self.hint.save()
        self.client = Client()

    def test_get_latest_system_notification__latest_one(self):
        response = self.client.get(reverse('django_top_notify:latest_system_notification'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content.get("category"), "hint")

    def test_get_latest_system_notification__expired(self):
        self.hint.expired = True
        self.hint.save()
        response = self.client.get(reverse('django_top_notify:latest_system_notification'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content.get("category"), "alert")

    def test_get_latest_system_notification__none(self):
        self.hint.expired = True
        self.hint.save()
        self.alert.expired = True
        self.alert.save()
        response = self.client.get(reverse('django_top_notify:latest_system_notification'))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content, {})
