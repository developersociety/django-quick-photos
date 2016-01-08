from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'https://www.instagram.com/explore/tags/%s/' % (self.name,)


@python_2_unicode_compatible
class Photo(models.Model):
    photo_id = models.CharField(max_length=100, unique=True)
    user = models.CharField(max_length=30, db_index=True)
    image = models.URLField()
    image_width = models.PositiveIntegerField()
    image_height = models.PositiveIntegerField()
    image_file = models.ImageField(upload_to='quickphotos/photo', blank=True)
    created = models.DateTimeField(db_index=True)
    caption = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    link = models.URLField()
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.caption:
            return '%s - %s' % (self.user, truncatechars(self.caption, 50))
        else:
            return self.user

    def get_absolute_url(self):
        return self.link


@python_2_unicode_compatible
class Like(models.Model):
    user = models.CharField(max_length=30, db_index=True)
    photo = models.ForeignKey(Photo)

    class Meta:
        ordering = ('-photo',)
        unique_together = (
            ('user', 'photo'),
        )

    def __str__(self):
        return '%s' % (self.photo,)
