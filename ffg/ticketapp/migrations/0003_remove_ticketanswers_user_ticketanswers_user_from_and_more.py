# Generated by Django 4.1.4 on 2022-12-13 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketapp', '0002_ticket_time_create_ticketanswers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketanswers',
            name='user',
        ),
        migrations.AddField(
            model_name='ticketanswers',
            name='user_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL, verbose_name='От кого'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticketanswers',
            name='user_to',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL, verbose_name='Кому'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='New', max_length=255, verbose_name='Статус'),
        ),
    ]
