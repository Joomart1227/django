# Generated by Django 4.1.7 on 2023-03-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Выполнено ли'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(verbose_name='Крайний срок'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
