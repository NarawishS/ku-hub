from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes', blank=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f'{self.title}'

    def like_amount(self):
        return self.likes.count()

    def dislike_amount(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('kuhub:blog-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Blog title: %s, "%s"' % (self.blog, self.text)
