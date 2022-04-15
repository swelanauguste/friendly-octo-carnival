import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import User


class AssignedTo(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE, default=1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Incoming(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    author = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to="incoming_documents/", null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE, default=1)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(AssignedTo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("incoming:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.uid) + "-" + self.title)
        super(Incoming, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
