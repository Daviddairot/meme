from django.apps import AppConfig


class BloggerappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bloggerapp"


class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloggerapp'

    def ready(self):
        import your_app_name.signals