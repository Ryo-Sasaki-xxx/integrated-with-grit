# Generated by Django 3.0.5 on 2023-10-10 06:33

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import with_grit.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=50, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', with_grit.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='ゴールコンテント')),
                ('status', models.IntegerField(choices=[(0, 'waiting'), (1, 'working'), (2, 'completed')], default=1, verbose_name='状態')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': 'ゴール',
                'verbose_name_plural': 'ゴール',
                'db_table': 'goal',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='お問い合わせ内容')),
                ('name', models.CharField(max_length=200, verbose_name='お名前')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
            ],
            options={
                'verbose_name': 'お問い合わせ',
                'verbose_name_plural': 'お問い合わせ',
                'db_table': 'help',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='タスクコンテント')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='with_grit.Goal', verbose_name='ゴールコンテント')),
            ],
            options={
                'verbose_name': 'タスク',
                'verbose_name_plural': 'タスク',
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='If_then',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='if-then ルール')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='with_grit.Task', verbose_name='タスク名')),
            ],
            options={
                'verbose_name': 'if-thenルール',
                'verbose_name_plural': 'if-thenルール',
                'db_table': 'if_then',
            },
        ),
    ]
