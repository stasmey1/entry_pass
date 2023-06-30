import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'entry_pass.settings')

app = Celery('entry_pass')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_cars': {
        'task': 'cel.tasks.check_cars',
        'schedule': crontab(minute='*/0', hour='*/24'),
    },
}
