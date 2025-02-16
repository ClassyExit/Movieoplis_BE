from django.contrib import admin

# Register your models here.
from .models import ListItem

class ListItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    search_fields = ('title', 'type')
    list_filter = ('type',)
    


admin.site.register(ListItem, ListItemAdmin)