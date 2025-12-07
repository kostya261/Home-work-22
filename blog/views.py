from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article, Topic


# Create your views here.


class ArticleListView(ListView):
    """Просмотр списка статей"""
    model = Article
    template_name = 'blog/blog_content.html'
    context_object_name = 'all_articles'
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    """Детальный просмотр статьи"""
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self):
        # Получаем статью и увеличиваем счетчик просмотров
        obj = super().get_object()

        if hasattr(obj, 'views'):
            obj.views += 1
            obj.save()
        return obj


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Создаем статью"""
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        """Автоматически устанавливаем текущего пользователя как владельца"""
        user = self.request.user

        # Публикуем, только если пользователь модератор/админ
        if user.has_perm("blog.can_add_article"):
            form.instance.is_published = True
        else:
            form.instance.is_published = False

        form.instance.owner = user

        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Редактируем статью"""
    model = Article
    form_class = ArticleForm
    template_name = 'blog/edit_article.html'

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'article_id': self.object.id})

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ArticleForm
        if user.has_perm("article.can_unpublish_article") and user.has_perm("article.can_delete_article"):
            return ArticleForm
        raise PermissionDenied


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:blog')
    pk_url_kwarg = 'article_id'

    def dispatch(self, request, *args, **kwargs):
        # 1. Получаем продукт
        article = self.get_object()

        # 2. Проверяем по ПРОСТОЙ логике
        user = request.user

        # 3. Три условия через ИЛИ
        is_owner = article.owner == user
        is_superuser = user.is_superuser
        is_in_moderator_group = user.groups.filter(name='Moderators').exists()
        is_in_admin_group = user.groups.filter(name='Administrators').exists()

        can_delete = is_owner or is_superuser or is_in_moderator_group or is_in_admin_group

        # 4. Если нельзя - возвращаем ошибку
        if not can_delete:
            from django.shortcuts import redirect
            return redirect('blog:blog')

        # 5. Если можно - пускаем дальше
        return super().dispatch(request, *args, **kwargs)


# Может быть потом
"""class ArticlesByTopycView(ListView):
    template_name = 'blog/articles_by_topic.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, id=self.kwargs['topic_id'])
        return Article.objects.filter(topic=self.topic, is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.topic
        return context"""
