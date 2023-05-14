from django.db import models

# Create your models here.
# posts/models.py


from django.db import models
from django.urls import reverse


class Post(models.Model):
  name = models.CharField(max_length=224, null=False, blank=False)
  content = models.TextField(max_length=254, null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.content

  def get_absolute_url(self):
    return reverse('posts:list-posts', kwargs={})