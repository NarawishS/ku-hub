from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f'{self.blog_title}'
