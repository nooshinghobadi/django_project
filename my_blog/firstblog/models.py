from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    class Status(models.TextChoices):
        draft='df','draft'
        published='pb','published'
    
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=50)
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.draft)

    class Meta:
        ordering=['-publish']
        indexes=[
           models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

