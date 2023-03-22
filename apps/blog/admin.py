from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    fields = ('title', 'slug', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        super().save_model(request, obj, form, change)
