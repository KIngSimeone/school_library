from .models import Admin, Manager, Student
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

def create_manager(first_name, last_name, user_name, password):
    try:
        manager = Manager.objects.create(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=make_password(password),
        )
        return manager

    except Exception as e:
        logger.error("create_manager@error")
        logger.error(e)
        return None

def get_all_managers():
    try:
        managers = Manager.objects.all()
        return managers

    except Exception as e:
        logger.error("get_all_managers@error")
        logger.error(e)
        return None

def create_student(first_name, last_name, user_name, password):
    try:
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            password=make_password(password),
        )
        return student

    except Exception as e:
        logger.error("create_student@error")
        logger.error(e)
        return None

def get_all_students():
    try:
        students = Student.objects.all()
        return students

    except Exception as e:
        logger.error("get_all_students@error")
        logger.error(e)
        return None