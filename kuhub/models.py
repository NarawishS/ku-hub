from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes', blank=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return str(self.title)

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
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def like_amount_comment(self):
        return self.likes.count()

    def dislike_amount_comment(self):
        return self.dislikes.count()

    def __str__(self):
        return 'Blog title: %s, "%s"' % (self.blog, self.text)

      
class BlogReport(models.Model):
    TOPIC_CHOICES = (
        ('Fake new', 'Fake new'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'), ('Threat', 'Threat'),
        ('Violence', 'Violence'), ('Indecent words', 'Indecent words'), ('Sexual Harassment', 'Sexual Harassment'),
        ('Others', 'Others')
    )

    blog = models.ForeignKey(Blog, related_name="reports", on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[Blog: %s] Topic: "%s" reported by %s, %s' % (self.blog, self.topic, self.author, self.pub_date)


class CommentReport(models.Model):
    TOPIC_CHOICES = (
        ('Fake new', 'Fake new'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'), ('Threat', 'Threat'),
        ('Violence', 'Violence'), ('Indecent words', 'Indecent words'), ('Sexual Harassment', 'Sexual Harassment'),
        ('Others', 'Others')
    )

    comment = models.ForeignKey(Comment, related_name="reports", on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[%s] Topic: "%s" reported by %s, %s' % (self.comment, self.topic, self.author, self.pub_date)
