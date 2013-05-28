from django.test import TestCase

from .models import BlogPost


class BlogPostTestCase(TestCase):
    def test_published_blogpost(self):
        from django.utils import timezone
        blogpost = BlogPost.objects.create(publish_date=timezone.now())
        self.assertTrue(blogpost.is_published)
        self.assertIn(blogpost, BlogPost.objects.published())
    
    def test_unpublished_blogpost(self):
        blogpost = BlogPost.objects.create(publish_date=None)
        self.assertFalse(blogpost.is_published)
        self.assertNotIn(blogpost, BlogPost.objects.published())
