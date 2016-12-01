from worker import app
from worker.utils import Mailer

@app.task
def send_mail(recipient, subject, body):
    mailer = Mailer(app.conf)
    return mailer.send(recipient=recipient, subject=subject, body=body)