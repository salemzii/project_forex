from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['date']

    def __str__(self):
        return self.name
