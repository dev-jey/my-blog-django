from django.contrib import admin

# Register your models here.

from app.models import Article, User, Category

class ArticleAdmin(admin.ModelAdmin):
    # exclude = ('minute_read',)
    pass
admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # exclude = ('minute_read',)
    pass
admin.site.register(Category, CategoryAdmin)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

admin.site.site_header = "Dev-Jey"
admin.site.site_title = "Dev-Jey"