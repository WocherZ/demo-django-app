from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

USER_GROUPS = (
    ('ADMIN', 'admin'),
    ('OPERATOR', 'operator'),
    ('VISITOR', 'visitor')
)

class VisitorManager():
    def _create_user(self, name, login, password, **extra_fields):
        visitor = self.model(
            login=login,
            name=name,
        )
        visitor.set_password(password)
        visitor.save(using=self._db)
        return visitor

    def create_user(self, name, login, password, **extra_fields):
        extra_fields.setdefault('group', USER_GROUPS[0][0])
        return self._create_user(name, login, password, **extra_fields)



class Visitor(AbstractBaseUser):
    name = models.CharField(max_length=32, verbose_name='Имя')
    login = models.CharField(max_length=32, unique=True, verbose_name='Логин')
    group = models.CharField(max_length=32, choices=USER_GROUPS, verbose_name='Группа пользователя')

    objects = VisitorManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name', 'password']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        permissions = []
