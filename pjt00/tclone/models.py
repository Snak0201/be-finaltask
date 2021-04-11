from django.db import models
from django.contrib.auth import get_user_model

class FF(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='ff_user'
    )
    followed = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='ff_followed'
    )
    class Meta:
        unique_together = ['user', 'followed']

    def __str__(self):
        return str(self.user)
