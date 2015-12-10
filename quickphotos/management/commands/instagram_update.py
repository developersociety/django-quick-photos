from django.conf import settings
from django.core.management.base import BaseCommand
from instagram.client import InstagramAPI

from quickphotos.utils import update_photos


def update_users(users, download):
    api = InstagramAPI(
        access_token=settings.INSTAGRAM_ACCESS_TOKEN,
        client_secret=settings.INSTAGRAM_CLIENT_SECRET)

    for user in users:
        recent_media, next = api.user_recent_media(user_id=user)
        update_photos(photos=recent_media, download=download)


class Command(BaseCommand):
    args = 'user [user ...]'

    def add_arguments(self, parser):
        parser.add_argument('--download-photos', action='store_true')

    def handle(self, *args, **options):
        update_users(users=args, download=options['download_photos'])
