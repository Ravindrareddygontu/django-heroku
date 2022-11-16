from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User, editable=False)
    Title = models.CharField(max_length=30)
    Opinion = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.Title


