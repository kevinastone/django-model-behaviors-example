from django.utils import timezone
from .models import BlogPost

# General ORM interaction
BlogPost.objects.filter(author__username='username1').filter(publish_date__lte=timezone.now())

# ORM Interaction with custom manager
BlogPost.objects.published()

# chained ORM interaction with custom manager
BlogPost.objects.published().filter(author__username='username1')

# chained ORM interaction with custom manager at tail (will fail without custom queryset)
BlogPost.objects.filter(author__username='username1').published()

# chained ORM with multiple custom queryset methods
BlogPost.objects.authored_by('username1').published()
type(BlogPost.objects.authored_by('username1'))
