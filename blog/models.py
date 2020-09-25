from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to='post/')
    likes = models.ManyToManyField(User, related_name='post_likes')


    def __str__(self):
        return self.title[0:30]+'...'

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 670:
            output_size = (500, 670)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Trending(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    trending = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.post.title[0:15] + '...  | ' + self.post.author.username

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='commenter', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:20] + '... | ' + self.post.title[:20] + '... | ' + self.user.username
