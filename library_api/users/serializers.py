from .models import Admin, Manager, Student
from rest_framework import serializers


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'first_name', 'last_name', 'user_name',
                  'created_at', 'updated_at']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'user_name',
                  'created_at', 'updated_at']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'user_name',
                  'created_at', 'updated_at']
