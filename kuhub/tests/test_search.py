from django.test import TestCase
from kuhub.models import *


class SearchViewTest(TestCase):
    USER1 = "keyboard2543"
    TAG1 = "nakadashi"

    def setUp(self) -> None:
        """Set up for searching."""
        self.user1 = User.objects.create(
            username="keyboard2543",
            first_name="Sahatsawat",
            last_name="Kanpai",
            email="keyboard2543@gmail.com",
            password="3452draobyek"
        )
