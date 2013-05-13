from django.test import TestCase

from .models import BlogPost


class BlogPostTestCase(TestCase):
    def test_published_blogpost(self):
        from django.utils import timezone
        blogpost = BlogPost.objects.create(publish_date=timezone.now())
        self.assertTrue(blogpost.is_published)
        self.assertIn(blogpost, BlogPost.objects.published())
