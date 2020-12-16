from django.test import TestCase
from kuhub.models import *


class SearchViewTest(TestCase):

    def setUp(self) -> None:
        """Set up for searching."""
        self.user1 = User.objects.create_user(
            username="keyboard2543",
            first_name="Sahatsawat",
            last_name="Kanpai",
            email="keyboard2543@gmail.com",
            password="3452draobyek"
        )
        self.user1.save()
        self.client.login(username=self.user1.username, password=self.user1.password)

        self.blog1 = Blog.objects.create(
            title="shibirinasai!?",
            short_description="Lisa voice!?",
            author=self.user1,
            tags=TaggableManager()
        )
        self.blog1.tags.name = "nakadashi"
        self.blog1.save()

    def test_searching_with_blog_title(self) -> None:
        keyword = self.blog1.title
        response = self.client.get(reverse('kuhub:blog-search'), {'keyword': keyword})
        self.assertContains(response, keyword)

    def test_searching_with_blog_description(self) -> None:
        keyword = self.blog1.short_description
        response = self.client.get(reverse('kuhub:blog-search'), {'keyword': keyword})
        self.assertContains(response, keyword)

    def test_searching_with_username(self) -> None:
        keyword = self.user1.username
        response = self.client.get(reverse('kuhub:blog-search'), {'keyword': keyword})
        self.assertContains(response, keyword)

    def test_searching_with_a_tag_name(self) -> None:
        keyword = self.blog1.tags.name
        response = self.client.get(reverse('kuhub:blog-search'), {'keyword': keyword})
        self.assertContains(response, keyword)
