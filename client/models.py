from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=150, verbose_name='Email')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
