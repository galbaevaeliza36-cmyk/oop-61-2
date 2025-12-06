from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    # НОВОЕ ПОЛЕ
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # Если удалить категорию, посты не удалятся
        null=True,  # Разрешаем полю быть пустым
        blank=True,
        verbose_name="Категория"
    )


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-pub_date']  # Сортировка (новые сверху)


