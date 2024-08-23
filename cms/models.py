from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    snapshot = models.TextField()
    detail = HTMLField()  # Use TinyMCE's HTMLField for rich text

    def __str__(self):
        return self.title
