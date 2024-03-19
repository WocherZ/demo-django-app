from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model

from app.models import TemperatureSensor

USER_GROUPS = (
    ('ADMIN', 'admin'),
    ('OPERATOR', 'operator'),
    ('VISITOR', 'visitor')
)

STATUS_CHOICES = (
    ('Оплачено', 'оплачено'),
    ('На оплате', 'на оплате'),
    ('Неоплачено', 'неоплачено'),
)

class VisitorManager(BaseUserManager):
    def create_user(self, login, password, name):
        visitor = self.model(
            login=login,
            name=name,
        )
        visitor.set_password(password)
        print(visitor.password)

        visitor.group = 'VISITOR'
        visitor.is_staff = False
        visitor.is_superuser = False
        visitor.save(using=self._db)
        return visitor


    def create_superuser(self, login, password, name='default-admin-name'):
        print("create_superuser")
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
    name = models.CharField(max_length=32, verbose_name='Имя')
    login = models.CharField(max_length=32, unique=True, verbose_name=' Логин')
    group = models.CharField(max_length=32, choices=USER_GROUPS, verbose_name='Группа пользователя', default='VISITOR')
    is_staff = models.BooleanField(default=False)
    balance = models.FloatField(
        validators=[MinValueValidator(0.0)],
        default=0.0
    )
    tariff = models.FloatField(
        validators=[MinValueValidator(0.0)],
        default=3.16
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Неоплачено')
    consumed_energy = models.FloatField(
        validators=[MinValueValidator(0.0)],
        default=0
    )
    sensor_id = models.ForeignKey(TemperatureSensor, on_delete=models.SET_DEFAULT, default=0)

    objects = VisitorManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        permissions = []

    def get_sensor(self):
        return TemperatureSensor.objects.get(sensor_id=self.sensor_id.sensor_id).sensor_id
