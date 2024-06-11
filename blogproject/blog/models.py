from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator,ValidationError
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostVideo(models.Model):
    post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    video = models.FileField(upload_to='videos/',validators=[
        FileExtensionValidator(allowed_extensions=['mp4','WMV'])
    ])
    def clean(self):
        self.file_size_validator()
    def file_size_validator(self):
        limit = 100 * 1024 * 1024
        if self.video.size > limit:
            raise ValidationError("fayl hajmi 100 mb dan oshmasligi kerak")


    def __str__(self):
        return f"Video for {self.post.title}"

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
