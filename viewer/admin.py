from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

class MovieAdmin(ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description="None")

    
    list_display = ['id', 'title', 'genre']
    ordering = ['title']
    list_display_links = ['id', 'title']
    list_per_page = 5
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']

    fieldsets = [
    (None, {'fields': ['title', 'created']}),
    (
      'External Information',
      {
        'fields': ['genre', 'released'],
        'description': (
          'These fields are going to be filled with data parsed '
          'from external databases.'
        )
      }
    ),
    (
      'User Information',
      {
        'fields': ['rating', 'description'],
        'description': 'These fields are intended to be filled in by our users.'
      }
    )
    ]
    readonly_fields = ['created']


# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)


