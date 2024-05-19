from django.contrib import admin
from apps.base import models

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'insta','facebook','email','phone')
    search_fields = ('title', 'insta','facebook','email','phone')
admin.site.register(models.Settings, SettingsFilterAdmin)

admin.site.register(models.Instagram)

admin.site.register(models.Images)

class WhyChooseUsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
admin.site.register(models.WhyChooseUs, WhyChooseUsFilterAdmin)

class WhatDoWeOfferFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
admin.site.register(models.WhatDoWeOffer, WhatDoWeOfferFilterAdmin)