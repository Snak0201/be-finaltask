from django.contrib.auth import get_user_model
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    tweet = models.TextField(max_length=140)
    def publish(self):
        self.save()
    def __str__(self):
        return self.tweet
