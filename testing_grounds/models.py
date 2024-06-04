from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text_content = models.TextField()

    def __str__(self):
        return self.title
    

