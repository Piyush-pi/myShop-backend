"""User app Model File"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    """
    Base Model class to add a id, created_at and updated_at field as common
    for all models. properties: id (uuid), created_at, updated_at (timestamp),
    is_deleted
    """
    class Meta:
        """Model Meta class Info."""
        abstract = True

    objects = models.Manager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        """Object String Representation"""
        return f"{self.id}-{self.created_at}"


class User(AbstractUser, BaseModel):
    # Add additional fields here
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)

    # You can add more fields as needed

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
