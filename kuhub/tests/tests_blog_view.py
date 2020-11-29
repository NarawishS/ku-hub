from django.test import TestCase

from kuhub.models import *
from kuhub.views import *


class BlogViewTests(TestCase):
    def test_index_page_no_blog(self):
        response = self.client.get(reverse('kuhub:blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "all blog")
