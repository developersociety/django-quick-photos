from django.contrib import admin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created')
    list_filter = ('created',)
    date_hierarchy = 'created'
    readonly_fields = (
        'photo_id', 'user', 'image', 'created', 'caption', 'link', 'like_count', 'comment_count')
    fieldsets = (
        (None, {
            'fields': readonly_fields,
        }),
    )

    def has_add_permission(self, request):
        return False
