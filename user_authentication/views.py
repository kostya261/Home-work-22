from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from config import settings
from .forms import CustomUserCreationForm, UserProfileForm
from .models import User


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'user_authentication/login.html'
    success_url = reverse_lazy('catalog:home')

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('catalog:home') # Перенаправление на другую страницу после выхода


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_authentication/register.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Сохраняем пользователя и отправляем приветственное письмо"""
        # Сохраняем пользователя
        response = super().form_valid(form)
        user = form.instance

        # Автоматически логиним пользователя после регистрации (опционально)
        # login(self.request, user)

        # Отправляем приветственное письмо
        self.send_welcome_email(user)

        return response

    def send_welcome_email(self, user):
        """Отправка приветственного письма"""
        subject = 'Добро пожаловать на наш сайт!'
        message = f"""
        Здравствуйте, {user.first_name or 'Уважаемый пользователь'}!

        Добро пожаловать на наш сайт! Ваша регистрация прошла успешно.

        Ваши данные для входа:
        Email: {user.email}

        Спасибо, что присоединились к нам!

        С уважением,
        Команда сайта
        """

        # Отправляем email
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,  # если True, ошибки не будут показываться
        )



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования профиля пользователя"""
    model = User
    form_class = UserProfileForm  # используй свою форму
    template_name = 'user_authentication/edit_profile.html'
    success_url = reverse_lazy('users:profile')

    # Этот метод гарантирует, что пользователь редактирует свой профиль
    def get_object(self, queryset=None):
        return self.request.user

    # Можно добавить дополнительные данные в контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        return context


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Класс для просмотра профиля"""
    model = User
    template_name = 'user_authentication/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user