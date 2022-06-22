from django.db.models.signals import post_migrate
from .models import Admin
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.apps import AppConfig

def create_required_object(sender, **kwargs):
    user_name = settings.SUPER_ADMIN_USER_NAME
    password = settings.SUPER_ADMIN_PASSWORD
    hashed_password = make_password(password)
    if not Admin.objects.filter(user_name=user_name).exists():
        Admin.objects.create(user_name=user_name, password= hashed_password)

class UsersConfig(AppConfig):
    name = 'users'

def ready(self):
    post_migrate.connect(create_required_object ,sender=self)