from django.contrib import admin
from articles.models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')
    search_fields = ('title', 'author', 'body')

admin.site.register(Articles, ArticleAdmin)
