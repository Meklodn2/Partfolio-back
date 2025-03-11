from django.db import models
from ckeditor.fields import RichTextField
from tags.models import Tag
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')

    class Meta:
        ordering = [ '-date_posted']
        verbose_name ='Post'
        verbose_name_plural = 'Posts'

