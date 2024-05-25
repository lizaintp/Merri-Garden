from django.contrib import admin
from apps.base import models

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'insta','facebook','email','phone')
    search_fields = ('title', 'insta','facebook','email','phone')
admin.site.register(models.Settings, SettingsFilterAdmin)

admin.site.register(models.Instagram)
class WhyChooseUsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
admin.site.register(models.WhyChooseUs, WhyChooseUsFilterAdmin)

admin.site.register(models.WhyChooseUsImage)

admin.site.register(models.About)
admin.site.register(models.AboutAbout)

class WhatDoWeOfferFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
admin.site.register(models.WhatDoWeOffer, WhatDoWeOfferFilterAdmin)

admin.site.register(models.WhatDoWeOfferImage)

class CommentsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )
admin.site.register(models.Comments, CommentsFilterAdmin)