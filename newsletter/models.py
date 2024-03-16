from django.db import models

from client.models import Client

NULLABLE = {'blank': True, 'null': True}


class NewsLetter(models.Model):

    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('sent', 'Запущена'),
        ('ended', 'Окончена'),
    ]

    scheduled_time = models.TimeField(verbose_name='Время рассылки')
    frequency = models.CharField(choices=FREQUENCY_CHOICES, max_length=10, verbose_name='Периодичность')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='created', verbose_name='Статус рассылки')
    is_sent = models.BooleanField(default=False)
    client = models.ManyToManyField(Client, verbose_name='Клиент')

    def __str__(self):
        return f"{self.status}, {self.client}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):

    theme = models.CharField(max_length=50, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f"{self.theme}, {self.text}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(models.Model):

    mailing_list = models.ForeignKey(NewsLetter, on_delete=models.CASCADE, verbose_name='Рассылка')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время рассылки')
    status_try = models.CharField(max_length=100, verbose_name='Статус попытки')
    response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f"{self.mailing_list} - {self.date_time}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
