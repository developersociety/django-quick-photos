from django import template

from quickphotos.models import Photo

register = template.Library()


@register.assignment_tag
def get_latest_photos(*args, **kwargs):
    limit = kwargs.pop('limit', None)
    photos = Photo.objects.all()

    if args:
        photos = photos.filter(user__in=args)

    if limit is not None:
        photos = photos[:limit]

    return photos
