from django.test import TestCase
from django.utils import timezone
from kuhub.models import *
from kuhub.views import *
from django.urls import reverse


class UserFeaturesTests(TestCase):
    """A User features tests."""

    def setUp(self) -> None:
        """Set up user account"""
        self.user = User.objects.create_user('User1',
                                        email='User1@ku.th',
                                        password='Himitsu1')

        self.user.first_name = "Wanderer"
        self.user.last_name = "Frog"
        self.user.save()

        self.client.login(username='User1', password='Himitsu1')

    def test_login(self) -> None:
        """User login status"""
        # collectstatic first
        response = self.client.get(reverse('kuhub:blog-home'))
        self.assertEqual(response.status_code, 200)

    def test_add_blog(self) -> None:
        """Adding user's blog post"""
        blog = Blog(title="Test case1", short_description="Description1",
                    body="Greeting1", pub_date=timezone.now())

        self.assertIs(blog.is_published(), True)
        self.assertEqual(blog.short_description, "Description1")

    def test_add_comment(self) -> None:
        """Adding user's comment post"""

        blog = Blog(title="Test case1", short_description="Description1",
                    body="Greeting1", pub_date=timezone.now())

        comment = Comment(blog=blog, text="Comment1", pub_date=timezone.now())

        self.assertIs(comment.is_published(), True)
        self.assertEqual(comment.text, "Comment1")

