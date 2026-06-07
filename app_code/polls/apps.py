from django.apps import AppConfig
import os

class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        from django.contrib.auth.models import User
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password=os.environ.get('DJANGO_APP_ADMIN_PASSWORD', 'admin')
                )
        except Exception:
            pass