from django.contrib import admin
from .models import Watch

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'release_date', 'image')
    fields = ('brand', 'model', 'description', 'price', 'release_date', 'image')
    # list_filter = ('brand')


