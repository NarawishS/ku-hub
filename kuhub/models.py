from django.db import models

from django.contrib.auth.models import User


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



