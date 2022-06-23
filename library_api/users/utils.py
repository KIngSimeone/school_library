from .models import Admin
from django.contrib.auth.hashers import make_password
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



def create_admin(first_name, last_name, user_name, password):
    try:
        admin = Admin.objects.create(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=make_password(password),
        )
        return admin

    except Exception as e:
        logger.error("create_admin@error")
        logger.error(e)
        return None

def get_all_admins():
    try:
        admins = Admin.objects.all()
        return admins

    except Exception as e:
        logger.error("get_all_admins@error")
        logger.error(e)
        return None