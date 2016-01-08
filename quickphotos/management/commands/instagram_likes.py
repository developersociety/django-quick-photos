from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from instagram.client import InstagramAPI

from quickphotos.utils import update_likes


@transaction.atomic
def update_user_likes(download):
    api = InstagramAPI(
        access_token=settings.INSTAGRAM_ACCESS_TOKEN,
        client_secret=settings.INSTAGRAM_CLIENT_SECRET)

    # Figure out the logged in user
    user = api.user()
    username = user.username

    # Find the media the user has liked
    liked_media, next = api.user_liked_media()
    update_likes(user=username, photos=liked_media, download=download)


class Command(BaseCommand):
    help = 'Download and store the latest liked photos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--download-photos', action='store_true',
            help='Download images from photos and store locally')

    def handle(self, **options):
        update_user_likes(download=options['download_photos'])
