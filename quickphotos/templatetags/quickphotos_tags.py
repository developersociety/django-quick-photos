from django import template

from quickphotos.models import Photo

register = template.Library()


@register.assignment_tag
def get_latest_photos(user, limit=None):
    photos = Photo.objects.filter(user=user)

    if limit is not None:
        photos = photos[:limit]

    return photos
