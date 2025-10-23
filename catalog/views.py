from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    """Коннектор для отображения страницы home.html"""
    return render(request, 'home.html')


def contacts(request):
    """Коннектор для отображения страницы contacts.html и обработки POST запроса"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        print(name)
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')
