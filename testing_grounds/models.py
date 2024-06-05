from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text_content = models.TextField()
    pub_date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text_content = models.TextField()
    pub_date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.text_content


