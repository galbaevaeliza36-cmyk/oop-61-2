

from django.contrib import admin
from .models import (Post, Category) # <-- Добавляем Category
admin.site.register(Post)
admin.site.register(Category) # <-- Регистрируем Category




