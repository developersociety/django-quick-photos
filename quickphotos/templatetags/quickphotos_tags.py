from django import template
from quickphotos.models import Photo

register = template.Library()


@register.assignment_tag
def get_latest_photos(user, amount=None):
    photos = Photo.objects.filter(user=user)

    if amount is not None:
        photos = photos[:amount]

    return photos
