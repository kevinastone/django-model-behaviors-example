from django.db import models


class PublishableQuerySet(models.query.QuerySet):
    def published(self):
        from django.utils import timezone
        return self.filter(~models.Q(publish_date=None)).filter(publish_date__lte=timezone.now())


class AuthorableQuerySet(models.query.QuerySet):
    def authored_by(self, author):
        return self.filter(author__username=author)
