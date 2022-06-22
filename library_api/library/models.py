from django.db import models


class BookCategory(models.Model):
    """Admin Model"""
    name = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']
