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
            name='Channel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=100000000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('singer', models.CharField(max_length=2000)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=100000)),
                ('song', models.FileField(upload_to='song')),
                ('movie', models.CharField(default='', max_length=1000)),
                ('is_junior_song', models.BooleanField(default=False)),
                ('is_juniorplus_song', models.BooleanField(default=False)),
                ('is_senior_song', models.BooleanField(default=False)),
                ('is_classical_song', models.BooleanField(default=False)),
                ('is_rock_song', models.BooleanField(default=False)),
                ('is_pop_song', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Listenlater',
            fields=[
                ('listen_id', models.AutoField(primary_key=True, serialize=False)),
                ('listen_music_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('favourites_id', models.AutoField(primary_key=True, serialize=False)),
                ('fmusic_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]