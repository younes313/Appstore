from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string

from app.models import App


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    unique_key = models.CharField(max_length=32, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.unique_key:
            self.unique_key = self.generate_unique_key()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_key():
        return get_random_string(32)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'app'], name='unique_purchase')
        ]
