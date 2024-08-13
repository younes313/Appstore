from django.contrib.auth.models import User
from django.db import models


class App(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons')
    is_verified = models.BooleanField(default=False)
    link = models.URLField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
