from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок поста')
    body = models.CharField(max_length=50, verbose_name='Текст поста')
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

