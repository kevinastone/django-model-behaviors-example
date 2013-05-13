from django.db import models
from django.contrib.auth.models import User


class BlogPostManager(models.Manager):
    
    def published(self):
        from django.utils import timezone
        return self.filter(publish_date__lte=timezone.now())
    
    def authored_by(self, author):
        return self.filter(author__username=author)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User, related_name='posts', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)
    
    objects = BlogPostManager()

    def pre_save(self, instance, add):
        from django.utils.text import slugify
        if not instance.slug:
            instance.slug = slugify(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog-post', (), {
            "slug": self.slug,
        })

    @property
    def is_published(self):
        from django.utils import timezone
        return self.publish_date < timezone.now()

    def publish_on(self, date=None):
        from django.utils import timezone
        if not date:
            date = timezone.now()
        self.publish_date = date
        self.save()
