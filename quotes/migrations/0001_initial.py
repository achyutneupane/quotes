# Generated by Django 3.0.6 on 2020-05-15 14:40

import ckeditor.fields
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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('status', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=400)),
                ('thumbdown', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='news')),
                ('description', ckeditor.fields.RichTextField()),
                ('page_visit', models.IntegerField(default=0)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('thumbdown', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='main_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.MainMenu'),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbup',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
