from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import make_aware, utc
from instagram.client import InstagramAPI
from quickphotos.models import Photo


def update_user(user):
    api = InstagramAPI(access_token=settings.INSTAGRAM_ACCESS_TOKEN)
    recent_media, next = api.user_recent_media(user_id=user)

    for i in recent_media:
        thumb = i.images['thumbnail']

        obj, created = Photo.objects.get_or_create(photo_id=i.id, defaults={
            'user': i.user.username,
            'thumb': thumb.url,
            'thumb_width': thumb.width,
            'thumb_height': thumb.height,
            'created': make_aware(i.created_time, utc),
            'caption': i.caption,
            'link': i.link,
        })


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in args:
            update_user(i)
