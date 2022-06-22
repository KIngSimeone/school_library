from django.db import models

class Admin(models.Model):
    """Admin Model"""
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email_address = models.EmailField(null=True)
    user_name = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']
