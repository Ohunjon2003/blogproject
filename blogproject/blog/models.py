from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostVideo(models.Model):
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    video = models.FileField(upload_to='media/videos',validators=[
        FileExtensionValidator(allowed_extensions=['mp4','WMV'])
    ])

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user} on {self.post}'
