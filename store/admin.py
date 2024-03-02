from django.contrib import admin
import admin_thumbnails
from .models import Store


# Store model Admin
@admin_thumbnails.thumbnail('image')
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortInfo', 'owner', 'phone', 'image_tag']


# Registration models
admin.site.register(Store, StoreAdmin)
