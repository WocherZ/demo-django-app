from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model

USER_GROUPS = (
    ('ADMIN', 'admin'),
    ('OPERATOR', 'operator'),
    ('VISITOR', 'visitor')
)

class VisitorManager(BaseUserManager):
    def create_user(self, login, password, name):
        visitor = self.model(
            login=login,
            name=name,
            password=password
        )
        visitor.set_password(password)
        visitor.group = 'VISITOR'
        visitor.is_staff = False
        visitor.is_superuser = False
        visitor.save(using=self._db)
        return visitor


    def create_superuser(self, login, password, name='default-admin-name'):
        visitor = self.create_user(login, password, name)
        visitor.group = 'ADMIN'
        visitor.is_active = True
        visitor.is_staff = True
        visitor.is_superuser = True
        visitor.save(using=self._db)
        return visitor


    def get_by_natural_key(self, login_):
        return self.get(login=login_)

class Visitor(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=32, default='DEFAULT_NAME', verbose_name='Имя')
    login = models.CharField(max_length=32, unique=True, verbose_name='Имя')
    group = models.CharField(max_length=32, choices=USER_GROUPS, verbose_name='Группа пользователя')
    is_staff = models.BooleanField(default=False)

    objects = VisitorManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        permissions = []
