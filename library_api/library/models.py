from unicodedata import category
from django.db import models
from users.models import Manager, Student


class BookCategory(models.Model):
    """BookCategory Model"""
    name = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']

class Book(models.Model):
    """Book Model"""
    name = models.TextField(null=True)
    author = models.TextField(null=True)
    date_published = models.DateField(null=True)
    category = models.ForeignKey(BookCategory, null=True, on_delete=models.SET_NULL)
    is_borrowed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        ordering = ['-created_at']


class BookRequest(models.Model):
    """BookRequest Model"""
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    status = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
    class Meta:
        ordering = ['-created_at']

class BorrowedBook(models.Model):
    """BorrowedBook Model"""
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-borrowed_at']