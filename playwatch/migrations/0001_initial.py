# Generated by Django 3.2.5 on 2022-04-14 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('director', models.CharField(max_length=2000)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=100000)),
                ('movie', models.FileField(upload_to='movie')),
                ('description', models.CharField(default='', max_length=1000)),
                ('is_junior_movie', models.BooleanField(default=False)),
                ('is_juniorplus_movie', models.BooleanField(default=False)),
                ('is_senior_movie', models.BooleanField(default=False)),
                ('is_action_movie', models.BooleanField(default=False)),
                ('is_thriller_movie', models.BooleanField(default=False)),
                ('is_comedy_movie', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WatchChannel',
            fields=[
                ('watch_channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('video', models.CharField(max_length=100000000)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlater',
            fields=[
                ('watch_id', models.AutoField(primary_key=True, serialize=False)),
                ('watch_video_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchFavourites',
            fields=[
                ('wfavourites_id', models.AutoField(primary_key=True, serialize=False)),
                ('fvideo_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
