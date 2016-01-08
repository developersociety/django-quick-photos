from django import template

from quickphotos.models import Photo, Tag

register = template.Library()


@register.assignment_tag
def get_latest_photos(*args, **kwargs):
    limit = kwargs.pop('limit', None)
    liked_by = kwargs.pop('liked_by', None)
    tag = kwargs.pop('tag', None)
    photos = Photo.objects.all()

    if liked_by:
        photos = photos.filter(like__user=liked_by)

    if tag:
        try:
            tag_obj = Tag.objects.get(name=tag)
            photos = photos.filter(tags=tag_obj)
        except Tag.DoesNotExist:
            photos = photos.none()

    if args:
        photos = photos.filter(user__in=args)

    if limit is not None:
        photos = photos[:limit]

    return photos
