from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=256,null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.name)


class TextSnippet(models.Model):
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, related_name='tag', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.text)

