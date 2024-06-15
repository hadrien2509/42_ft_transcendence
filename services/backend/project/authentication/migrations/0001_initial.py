# Generated by Django 5.0 on 2024-06-15 11:26

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('loss', models.IntegerField(default=0, verbose_name='number of lost game')),
                ('win', models.IntegerField(default=0, verbose_name='number of games won')),
                ('profile_pic', models.ImageField(default='default_pp.jpeg', upload_to='', verbose_name='profile pic')),
                ('is_online', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('language', models.CharField(default='eng')),
                ('friends', models.ManyToManyField(blank=True, related_name='friend_list', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('p1_score', models.IntegerField()),
                ('p2_score', models.IntegerField()),
                ('winner_id', models.IntegerField()),
                ('is_pong', models.BooleanField(default=False)),
                ('p1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_p1', to=settings.AUTH_USER_MODEL)),
                ('p2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_p2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MorpionParties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oponent', models.CharField(max_length=20, verbose_name='oponent')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date of the match')),
                ('winner', models.IntegerField(default=0, verbose_name='state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='morpion_parties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='score')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
