from worker import app
from worker.utils import Mailer


@app.task
def hello_world():
    mailer = Mailer(app.conf)
    mailer.send(recipient='petar.efnushev@keitaro.com',
                subject='Celery Periodic Task',
                body='Hello, World!')
