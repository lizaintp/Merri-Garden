from django.contrib import admin
from apps.secondary import models

# Register your models here.
class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'date')
    search_fields = ('title', 'date')
admin.site.register(models.Gallery, GalleryFilterAdmin)

class BandFilterAdmin(admin.ModelAdmin):
    list_filter = ('fullname', )
    list_display = ('fullname', 'profession')
    search_fields = ('fullname', 'profession')
admin.site.register(models.Band, BandFilterAdmin)

class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'date')
    search_fields = ('title', 'date')
admin.site.register(models.News, NewsFilterAdmin)

