from django.db import models
from django.contrib.auth.models import User

TOPIC_CHOICES = [
    ("science", "Science"),
    ("technology", "Technology"),
    ("politics", "Politics"),
    ("sports", "Sports"),
    ("space", "Space"),
    ("economy", "Economy"),
]


class Post(models.Model):
    topic = models.CharField(max_length=200, choices=TOPIC_CHOICES)
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='main_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.topic} by {self.author} at {self.created_on}"


class HomePost(models.Model):
    latest_image = models.ImageField(upload_to='latest_images/', null=True, blank=True)
    popular_image = models.ImageField(upload_to='popular_images/', null=True, blank=True)
    subscribe_image = models.ImageField(upload_to='subscribe_images/', null=True, blank=True)

    def __str__(self):
        return "HomePost images"

