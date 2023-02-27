from django.contrib import admin
from . models import BlogModel
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    # list_filter = ()
    search_fields = ['title', 'content']

admin.site.register(BlogModel, BlogAdmin)
