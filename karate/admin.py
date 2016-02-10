from django.contrib import admin

# Register your models here.

from .models import Articles, Photo, PhotoAlbum, PlanOfEvents, Videos  #, GroupUsers


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('dc', 'name', )
    list_filter = ('dc', 'name', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('dc', 'photo_album')
    list_filter = ('dc', 'photo_album')


class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ('dc', 'name')
    list_filter = ('dc', 'name')


class PlanOfEventsAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')
    list_filter = ('date', 'name')


class ViedeoAdmin(admin.ModelAdmin):
    list_display = ('name', 'dc')
    list_filter = ('name', 'dc')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(PlanOfEvents, PlanOfEventsAdmin)
# admin.site.register(Videos,ViedeoAdmin)
admin.site.register(Videos)

