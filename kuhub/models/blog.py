from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class BlogForum(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField(blank=True)
    body = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='blog_dislikes', blank=True)
    forum = models.ForeignKey(BlogForum, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

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
