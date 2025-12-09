from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import EmailValidator, RegexValidator
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    """Кастомный менеджер для модели User без username."""

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает пользователя с email и паролем."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и возвращает суперпользователя."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    email = models.EmailField(
        verbose_name='Email адрес',
        unique=True,
        blank=False,
        null=False,
        validators=[EmailValidator()],
        error_messages={
            'unique': 'Пользователь с таким email уже существует.',
        },
        help_text='Обязательное поле. Используется для входа в систему.'
    )

    # Аватар (изображение)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='users/avatars/',
        blank=True,
        null=True,
        help_text='Загрузите ваш аватар'
    )

    # Номер телефона с валидацией
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+79999999999'. До 15 цифр."
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        help_text='Введите номер телефона'
    )

    # Страна
    country = models.CharField(
        verbose_name='Страна',
        max_length=100,
        blank=True,
        null=True,
        help_text='Введите вашу страну'
    )

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
