from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Отображаем заголовок, автора и дату создания
    list_filter = ('created_at',)  # Добавляем фильтр по дате создания
    search_fields = ('title', 'text')  # Добавляем возможность поиска по заголовку и содержимому

    def created_at(self, obj):
        return obj.created_at  # Используем поле created_at для отображения

    created_at.admin_order_field = 'created_at'  # Позволяет сортировать по дате создания
    created_at.short_description = 'Дата создания'  # Название колонки в админке

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')  # Отображаем пост, автора и дату создания
    list_filter = ('created_at',)  # Добавляем фильтр по дате создания
    search_fields = ('text',)  # Добавляем возможность поиска по тексту комментария

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)