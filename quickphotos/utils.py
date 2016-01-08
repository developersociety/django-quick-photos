import hashlib
from tempfile import TemporaryFile

from django.core.files import File
from django.utils.timezone import make_aware, utc
from PIL import Image
import requests

from .models import Like, Photo, Tag


def photo_tags(obj, tags):
    for tag in tags:
        name = tag.name.lower()

        # No sane limit on tags - so we enforce one here by avoiding them
        if len(name) > 200:
            continue

        tag_obj, created = Tag.objects.get_or_create(name=name)

        obj.tags.add(tag_obj)


def update_photos(photos, download=False):
    obj_list = []

    for i in photos:
        image = i.images['standard_resolution']

        if i.caption:
            caption = i.caption.text
        else:
            caption = ''

        obj, created = Photo.objects.update_or_create(photo_id=i.id, defaults={
            'user': i.user.username,
            'image': image.url,
            'image_width': image.width,
            'image_height': image.height,
            'created': make_aware(i.created_time, utc),
            'caption': caption,
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

        # Add tags
        photo_tags(obj=obj, tags=i.tags)

        obj_list.append(obj)

    return obj_list


def update_likes(user, photos, download=False):
    obj_list = update_photos(photos=photos, download=download)

    for photo in obj_list:
        Like.objects.get_or_create(user=user, photo=photo)

    return obj_list
