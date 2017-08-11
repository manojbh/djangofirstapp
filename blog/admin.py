from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author','title','text']}),
        ('Date information', {'fields': ['created_date','published_date']}),
    ]
    inlines = [CommentInline]
    list_display = ('author', 'title','text', 'created_date','published_date')
    list_filter = ['created_date','published_date']
    search_fields = ['title','text']
    list_per_page = 3




admin.site.register(Post, PostAdmin)
admin.site.register(Comment)