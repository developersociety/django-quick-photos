from django.db import models
from django.template.defaultfilters import truncatechars


class Photo(models.Model):
    photo_id = models.CharField(max_length=100, unique=True)
    user = models.CharField(max_length=30, db_index=True)
    thumb = models.URLField()
    thumb_width = models.PositiveIntegerField()
    thumb_height = models.PositiveIntegerField()
    created = models.DateTimeField(db_index=True)
    caption = models.TextField()
    link = models.URLField()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s - %s' % (self.user, truncatechars(self.caption, 50))

    def get_absolute_url(self):
        return self.link
