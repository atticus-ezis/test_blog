from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    text_content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text_content = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text_content


