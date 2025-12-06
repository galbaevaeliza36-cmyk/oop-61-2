from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Post


class PostListView(ListView):
        model = Post
        template_name = 'posts/post_list.html'   # Шаблон списка постов
        context_object_name = 'posts'            # Имя переменной в шаблоне

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                # Прокидываем флаг и сообщение в шаблон
                context['raptor_mini_enabled'] = getattr(settings, 'RAPTOR_MINI_ENABLED', False)
                context['raptor_mini_message'] = getattr(settings, 'RAPTOR_MINI_MESSAGE', '')
                return context


class PostDetailView(DetailView):
        model = Post
        template_name = 'posts/post_detail.html' # Шаблон одного поста
        context_object_name = 'post'             # Имя переменной в шаблоне

