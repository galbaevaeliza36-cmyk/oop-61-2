from django.urls import path
from .views import PostListView, PostDetailView  # Импортируем наши Views

urlpatterns = [
    # Главная страница (список постов)
    path('', PostListView.as_view(), name='post-list'),

    # Страница одного поста (например, /post/1/)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
