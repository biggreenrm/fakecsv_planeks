from django.db import models
from django.conf import settings
from django.urls import reverse
import os


class DataSchema(models.Model):
    """Model which describes data schemas."""

    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("list_dataset", args=[self.id])


class Field(models.Model):
    """Model which describes fields needed to generate data set using chosen schema."""

    CHOICES = (
        ('Full name', 'Full name'),
        ('Job', 'Job'),
        ('Email', 'Email'),
        ('Domain name', 'Domain name'),
        ('Phone number', 'Phone number'),
        ('Company name', 'Company name'),
        ('Address', 'Address'),
        ('Date', 'Date'),
    )
    column_name = models.CharField(max_length=300)
    type = models.CharField(max_length=50, choices=CHOICES)
    order = models.PositiveIntegerField()
    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} of schema {self.schema}"


def csv_path():
    return os.path.join(settings.MEDIA_ROOT, 'datasets')

class DataSet(models.Model):
    """Model which describes CSV datasets accepted by using data-schema."""
    
    CHOICES = (
        ('Processing', 'Processing'),
        ('Ready', 'Ready'),
    )
    file = models.FilePathField(path=csv_path)
    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=CHOICES)

    def set_ready(self):
        self.status ='Ready'
        return self.status
