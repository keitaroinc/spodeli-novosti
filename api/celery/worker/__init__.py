# -*-coding:utf-8-*-
import os

from celery import Celery
from datetime import timedelta

# Load settings
settings = os.getenv(
    'WORKER_SETTINGS',
    'worker.config.DevelopmentConfig'
)

app = Celery(__name__)
app.config_from_object(settings)

# Register tasks
app.autodiscover_tasks(['worker.components.test',
                        'worker.components.email'])
