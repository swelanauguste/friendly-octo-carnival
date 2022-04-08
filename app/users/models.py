import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# from django.urls import reverse


class User(AbstractUser):
    is_viewer = models.BooleanField(default=True)
    is_creator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Department(models.Model):
    agency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.agency_name


class UserProfile(models.Model):
    GENDER_LIST = [
        ("M", "M"),
        ("F", "F"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=65, blank=True)
    last_name = models.CharField(max_length=65, blank=True)
    agency = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="agencies", null=True, blank=True
    )
    slug = models.SlugField(max_length=65, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField("DOB", blank=True, null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=25, blank=True, default="+ 1758")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
