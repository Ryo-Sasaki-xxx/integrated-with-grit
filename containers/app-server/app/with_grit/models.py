from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力して下さい')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=Trueである必要があります。')
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField("username", max_length=50, validators=[username_validator], blank=True)
    email = models.EmailField("email_address", unique=True)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Goal(models.Model):
    class Meta:
        db_table = 'goal'
        verbose_name = 'ゴール'
        verbose_name_plural = 'ゴール'
    
    status_list = [
        (0,'waiting'),
        (1,'working'),
        (2,'completed'),
    ]
    
    content = models.CharField(verbose_name='ゴールコンテント', max_length=200, )
    status = models.IntegerField(verbose_name='状態', choices=status_list, default='work',)
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE,)

    def __str__ (self):
        return self.content


class Task(models.Model):
    class Meta:
        db_table= 'task'
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'
    
    content = models.CharField(verbose_name='タスクコンテント', max_length=200, )
    goal = models.ForeignKey(Goal, verbose_name='ゴールコンテント', on_delete=models.CASCADE,)

    def __str__ (self):
        return self.content

class If_then(models.Model):
    class Meta:
        db_table='if_then'
        verbose_name='if-thenルール'
        verbose_name_plural = 'if-thenルール'

    content = models.CharField(verbose_name='if-then ルール', max_length=200, )
    task = models.OneToOneField(Task, verbose_name='タスク名', on_delete=models.CASCADE,)

    def __str__ (self):
        return self.content