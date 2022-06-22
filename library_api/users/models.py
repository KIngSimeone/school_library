from django.db import models

class Admin(models.Model):
    """Admin Model"""
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    user_name = models.TextField(null=True)
    password = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Manager(models.Model):
    """Manager Model"""
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    user_name = models.TextField(null=True)
    password = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Student(models.Model):
    """Manager Model"""
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    user_name = models.TextField(null=True)
    password = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']

class UserAccessTokens(models.Model):
    """UserAccessTokens Model"""
    user_id = models.TextField(null=True)
    access_token = models.TextField("access_token")

    expires_at = models.DateTimeField("expires_at")
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        verbose_name = "User Access Token"
        verbose_name_plural = "User Access Tokens"