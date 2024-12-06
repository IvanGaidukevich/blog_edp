from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    class Status(models.TextChoices):
        PUBLISHED = 'P', 'Published'
        DRAFT = 'D', 'Draft'

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст поста")
    published = models.DateTimeField(verbose_name="Дата публикации")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices,
                              default=Status.DRAFT, max_length=1)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('blog:get_post', args=[self.published.year,
                                              self.published.month,
                                              self.published.day,
                                              self.slug])



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


