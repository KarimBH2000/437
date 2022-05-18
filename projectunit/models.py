from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# This is the Post model, each post has a title, content, date posted and author (user's unique username)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Get post details (title content). Returns the post_detail.html page.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

