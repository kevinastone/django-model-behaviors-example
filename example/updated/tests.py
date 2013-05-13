from django.test import TestCase

from .models import BlogPost


class BehaviorTestCaseMixin(object):
    def get_model(self):
            return getattr(self, 'model')
    
    def create_instance(self, **kwargs):
        raise NotImplementedError("Implement me")


class PublishableTests(BehaviorTestCaseMixin):
    def test_published_blogpost(self):
        from django.utils import timezone
        obj = self.create_instance(publish_date=timezone.now())
        self.assertTrue(obj.is_published)
        self.assertIn(obj, self.model.objects.published())


class BlogPostTestCase(PublishableTests, TestCase):
    model = BlogPost
    
    def create_instance(self, **kwargs):
        return BlogPost.objects.create(**kwargs)


"""
class BlogPostTestCase(PublishableTests, AuthorableTests, PermalinkableTests, TimestampableTests, TestCase):
    model = BlogPost
    
    def create_instance(self, **kwargs):
        return BlogPost.objects.create(**kwargs)

    def test_blog_specific_functionality(self):
        ...
"""
