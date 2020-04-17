from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'advisor', 'is_published', 'list_date',)
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)

admin.site.register(Listing, ListingAdmin)

