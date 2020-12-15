from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from kuhub.models import Blog


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def like_amount_comment(self):
        return self.likes.count()

    def dislike_amount_comment(self):
        return self.dislikes.count()

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False

    def __str__(self):
        return 'Blog title: %s, "%s"' % (self.blog, self.text)


class CommentReport(models.Model):
    TOPIC_CHOICES = (
        ('Fake news', 'Fake news'), ('Spam', 'Spam'), ('Create conflict', 'Create conflict'), ('Threat', 'Threat'),
        ('Violence', 'Violence'), ('Indecent words', 'Indecent words'), ('Sexual Content', 'Sexual Content'),
        ('Others', 'Others')
    )

    comment = models.ForeignKey(Comment, related_name="reports", on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[%s] Topic: "%s" reported by %s, %s' % (self.comment, self.topic, self.author, self.pub_date)
