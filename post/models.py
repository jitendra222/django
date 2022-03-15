from unicodedata import name
from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta(object):
        db_table = 'Blogs'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=194, db_index=True, default='admin'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )     

    