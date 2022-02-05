# django-top-notify
[![license](https://img.shields.io/badge/license-mit-brightgreen.svg?style=flat)](https://github.com/normal-wls/django-top-notify/blob/main/LICENSE) [![Release Version](https://img.shields.io/badge/release-1.0.0-brightgreen.svg)](https://github.com/normal-wls/django-top-notify/releases)

A top notification bar based on Django project.

### Feature 
- Integrate into an existing Django project easily.
- Support `hint` and `alert` type of top notification.
- Publish and cancel top notification dynamically without deployment.
- Latest notification will automatically be displayed.

### Demo
- Publish or cancel

  Use Django Admin page to configure:

  ![configuration.png](docs/pics/configuration.png)

- Hint top notification

  ![hint_top_notification.png](docs/pics/hint_top_notification.png)

- Alert top notification

  ![alert_top_notification.png](docs/pics/alert_top_notification.png)

### Quick Start
- Install django-top-notify:
  ```shell
  # bash
  pip install django-top-notify
  ```
- Add `django_top_notify` into INSTALLED_APPS:
  ``` python
  # settings.py
  INSTALLED_APPS = [
      ...
      "django_top_notify",
      ...
  ]
  ```
- Add urls into urlpatterns:
  ``` python
  # urls.py
  urlpatterns = [
    ...
    path("top_notify/", include("django_top_notify.urls")),
    ...
  ]
  ```
- Collect static files & migrate:
  ```shell
  # bash
  python manage.py collectstatic
  python manage.py migrate django_top_notify
  ```
- Add frontend elements into template:
  ``` html
  <!--templates/index.html-->
  {% load static %}
  <head>
      <link rel="stylesheet" href="{% static 'django_top_notify/css/notification-top-bar.css' %}">
  </head>
  <body>
      <div class="notification-top-bar-container"><div class="notification-top-bar"><p></p></div></div>
      ...
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
      <script src="{% static 'django_top_notify/js/notification-top-bar.js' %}"></script>
      <script>
          $(function () {
              const url = "{% url 'django_top_notify:latest_system_notification' %}";
              get_latest_system_notification(url);
          })
      </script>
  </body>
  ```

### Donations
If this project helps you, please reward the author with a cup of coffee.（＾∀＾）

![donate_qr_code.png](docs/pics/donate_qr_code.png)