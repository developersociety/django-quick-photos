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
    help = 'Download and store the latest photos of followed users'

    def add_arguments(self, parser):
        parser.add_argument(
            'users', metavar='user', nargs='+',
            help='Instagram user ID to update')
        parser.add_argument(
            '--download-photos', action='store_true',
            help='Download images from photos and store locally')

    def handle(self, **options):
        update_users(users=options['users'], download=options['download_photos'])
