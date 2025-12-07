from django.urls import path

from blog import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', views.ArticleListView.as_view(), name='blog'),
    path('article_detail/<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article_delete/<int:article_id>/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('article_create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    # Потом как нибудь
    # path('topic/<int:topic_id>/', views.ArticlesByTopycView.as_view(), name='articles_by_topic'),
]
