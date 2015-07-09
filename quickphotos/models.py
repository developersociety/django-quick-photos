from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Photo(models.Model):
    photo_id = models.CharField(max_length=100, unique=True)
    user = models.CharField(max_length=30, db_index=True)
    image = models.URLField()
    image_width = models.PositiveIntegerField()
    image_height = models.PositiveIntegerField()
    created = models.DateTimeField(db_index=True)
    caption = models.TextField()
    link = models.URLField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.caption:
            return '%s - %s' % (self.user, truncatechars(self.caption, 50))
        else:
            return self.user

    def get_absolute_url(self):
        return self.link
