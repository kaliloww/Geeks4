from django.contrib import admin
from posts.models import Post


# Простой способ регистрации моделей в адмирнке
# admin.site.register(Post)


# развернетый способ
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'status']
    list_filter=['status']
    list_editable =['status']