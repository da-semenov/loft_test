# Generated by Django 3.2 on 2021-04-20 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название тэга')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.tag', verbose_name='Тэг')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name='Публикация')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
