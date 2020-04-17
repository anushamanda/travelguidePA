from django.contrib import admin
from .models import Advisor

class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'advisor_email')
    list_display_links = ('id', 'name')
    list_filter = ('name',)



admin.site.register(Advisor, AdvisorAdmin)

