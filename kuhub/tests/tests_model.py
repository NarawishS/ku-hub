"""Test model"""
from django.test import TestCase

from kuhub.models import *


class BlogModelTests(TestCase):
    """Testcase for Blog model"""

    def setUp(self):
        """Setup blog for test"""
        self.user = User.objects.create_user("user", "user@email.com", "12345")
        self.forum = BlogForum.objects.create(name="test-forum")
        self.blog = Blog.objects.create(title="title",
                                        body="body",
                                        author=self.user,
                                        forum=self.forum)

    def test_initial_like_and_dislike(self):
        self.assertEqual(0, self.blog.like_amount())
        self.assertEqual(0, self.blog.dislike_amount())

    def test_blog_in_forum(self):
        self.assertEqual(self.blog.forum, self.forum)

    def test_blog_author(self):
        self.assertEqual(self.blog.author, self.user)


class CommentModelTests(TestCase):

    def setUp(self):
        """Setup blog for test"""
        self.user = User.objects.create_user("user", "user@email.com", "12345")
        self.forum = BlogForum.objects.create(name="test-forum")
        self.blog = Blog.objects.create(title="title",
                                        body="body",
                                        author=self.user,
                                        forum=self.forum)
        self.comment = Comment.objects.create(blog=self.blog,
                                              text='text',
                                              author=self.user)

    def test_initial_like_and_dislike(self):
        self.assertEqual(0, self.comment.like_amount_comment())
        self.assertEqual(0, self.comment.dislike_amount_comment())

    def test_comment_in_blog(self):
        self.assertEqual(self.comment.blog, self.blog)

    def test_comment_author(self):
        self.assertEqual(self.comment.author, self.user)
