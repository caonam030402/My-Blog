from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    description = models.TextField()
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return f"Image {self.id}"
