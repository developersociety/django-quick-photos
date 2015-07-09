from django.utils.timezone import make_aware, utc

from .models import Photo


def update_photos(photos):
    for i in photos:
        thumb = i.images['thumbnail']

        obj, created = Photo.objects.get_or_create(photo_id=i.id, defaults={
            'user': i.user.username,
            'thumb': thumb.url,
            'thumb_width': thumb.width,
            'thumb_height': thumb.height,
            'created': make_aware(i.created_time, utc),
            'caption': i.caption or '',
            'link': i.link,
        })
