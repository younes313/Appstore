from django.db import models


class App(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons')
    is_verified = models.BooleanField(default=False)
    link = models.URLField(max_length=255)

    def __str__(self):
        return self.title
