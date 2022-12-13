from ffg.celery import app
from .models import Ticket

from celery import shared_task

@shared_task
def todo():
    ...