from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):
    """Модель для добавления темы в базу данных"""

    class Meta:
        model = Article
        fields = ['title', 'content', 'topic', 'image', 'is_published']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Содержание статьи'}),
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Название статьи',
            'content': 'Содержание',
            'topic': 'Тема',
            'image': 'Изображение',
        }
