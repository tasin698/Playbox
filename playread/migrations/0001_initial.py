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
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('author', models.CharField(max_length=2000)),
                ('tags', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=100000)),
                ('book', models.FileField(upload_to='book')),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Readchannel',
            fields=[
                ('read_channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('novel', models.CharField(max_length=100000000)),
            ],
        ),
        migrations.CreateModel(
            name='Readlater',
            fields=[
                ('read_id', models.AutoField(primary_key=True, serialize=False)),
                ('read_novel_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Readhistory',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('novel_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
