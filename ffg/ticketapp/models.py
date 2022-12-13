from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    status =  models.CharField(max_length=255, verbose_name='Статус', default='New')
    description = models.TextField(blank=False, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"

    def __str__(self):
        return self.name

class TicketAnswers(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from', verbose_name='От кого')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to', verbose_name='Кому')
    description = models.TextField(blank=False, verbose_name='Описание')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Тикет')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    

    class Meta:
        verbose_name = "Ответы"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.name
