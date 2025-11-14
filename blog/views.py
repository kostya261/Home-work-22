from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView

from blog.forms import ArticleForm
from blog.models import Article, Topic


# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/blog_content.html'
    context_object_name = 'all_articles'
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
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





class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'
    success_url = reverse_lazy('home')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/edit_article.html'

    def get_success_url(self):

        return reverse('blog:article_detail', kwargs={'article_id': self.object.id})


#Может быть потом
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