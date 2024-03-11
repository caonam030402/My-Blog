from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    description = models.TextField()
    content = MarkdownxField()
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title
    
class NhatKy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    description = models.TextField()
    content = MarkdownxField()
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image.name