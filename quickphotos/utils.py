import hashlib
from tempfile import TemporaryFile

from django.core.files import File
from django.db import transaction
from django.utils.timezone import make_aware, utc
from PIL import Image
import requests

from .models import Photo


@transaction.atomic
def update_photos(photos, download=False):
    obj_list = []

    for i in photos:
        image = i.images['standard_resolution']

        obj, created = Photo.objects.update_or_create(photo_id=i.id, defaults={
            'user': i.user.username,
            'image': image.url,
            'image_width': image.width,
            'image_height': image.height,
            'created': make_aware(i.created_time, utc),
            'caption': i.caption or '',
            'link': i.link,
            'like_count': i.like_count,
            'comment_count': i.comment_count,
        })

        if download and not obj.image_file:
            with TemporaryFile() as temp_file:
                image_file = File(temp_file)

                # Download the file
                r = requests.get(image.url, stream=True)
                r.raise_for_status()

                for chunk in r.iter_content(4096):
                    image_file.write(chunk)

                # Get Pillow to look at it
                image_file.seek(0)
                pil_image = Image.open(image_file)
                image_name = '%s.%s' % (
                    hashlib.md5(image.url.encode()).hexdigest(), pil_image.format.lower())

                # Save the file
                image_file.seek(0)
                obj.image_file.save(image_name, image_file, save=True)

        obj_list.append(obj)

    return obj_list
