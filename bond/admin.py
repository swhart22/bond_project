from django.contrib import admin

from bond.models import Article

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('headline',)}

admin.site.register(Article, ArticleAdmin)

# Register your models here.
