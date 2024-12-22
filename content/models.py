from django.db import models
from users.models import User
from .validators import validate_age, validate_title

NULLABLE = {"blank": True, "null": True}

class Post(models.Model):
    """
    Представляет собой блог-пост.

    Атрибуты:
        title (str): Заголовок поста.
        text (str): Содержимое поста.
        image (ImageField): Необязательное изображение, связанное с постом.
        author (ForeignKey): Пользователь, создавший пост.
        created_at (DateTimeField): Время создания поста.
        updated_at (DateTimeField): Время последнего обновления поста.
    """
    title = models.CharField(max_length=255, validators=[validate_title], help_text="Заголовок поста")
    text = models.TextField()
    image = models.ImageField(upload_to='posts/', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """Проверка возраста автора перед сохранением поста."""
        validate_age(self.author)

    def save(self, *args, **kwargs):
        """Переопределение метода save для вызова clean."""
        self.clean()  # Вызов метода clean перед сохранением
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Представляет собой комментарий к блог-посту.

    Атрибуты:
        post (ForeignKey): Пост, к которому принадлежит комментарий.
        author (ForeignKey): Пользователь, оставивший комментарий.
        text (str): Содержимое комментария.
        created_at (DateTimeField): Время создания комментария.
        updated_at (DateTimeField): Время последнего обновления комментария.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'Комментарий от {self.author} к {self.post}'