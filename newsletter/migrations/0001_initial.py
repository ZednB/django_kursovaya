# Generated by Django 5.0.3 on 2024-03-16 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_alter_client_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=50, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.TimeField(verbose_name='Время рассылки')),
                ('frequency', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=10, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('sent', 'Запущена'), ('ended', 'Окончена')], default='created', max_length=10, verbose_name='Статус рассылки')),
                ('is_sent', models.BooleanField(default=False)),
                ('client', models.ManyToManyField(to='client.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время рассылки')),
                ('status_try', models.CharField(max_length=100, verbose_name='Статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.newsletter', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]