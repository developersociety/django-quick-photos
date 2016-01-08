from django import template

from quickphotos.models import Photo

register = template.Library()


@register.assignment_tag
def get_latest_photos(*args, **kwargs):
    limit = kwargs.pop('limit', None)
    liked_by = kwargs.pop('liked_by', None)
    photos = Photo.objects.all()

    if liked_by:
        photos = photos.filter(like__user=liked_by)

    if args:
        photos = photos.filter(user__in=args)

    if limit is not None:
        photos = photos[:limit]

    return photos
