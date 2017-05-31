from django.contrib import admin
from shortener.models import Uri


@admin.register(Uri)
class UriAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode', 'updated', 'active')


# admin.site.register(Uri, UriAdmin)

