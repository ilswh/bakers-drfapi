from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cause = models.CharField(max_length=50)
    matter = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} : {self.reason}"
