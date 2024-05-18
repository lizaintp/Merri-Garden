from django.contrib import admin
from apps.contacts import models

# Register your models here.
class ContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name','email','subject')
    search_fields = ('name', 'insta','email','subject')
admin.site.register(models.Contacts, ContactsFilterAdmin)

class QuetionsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )
admin.site.register(models.Quetions, QuetionsFilterAdmin)