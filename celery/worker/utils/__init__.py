import logging
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

log = logging.getLogger(__name__)


class Mailer(object):
    def __init__(self, config):
        self.email_from = formataddr(
            (str(Header(config['FROM_NAME'], 'utf-8')),
             config['FROM_EMAIL'])
        )
        self.server_name = config['SMTP_SERVER']
        self._username = config['SMTP_SERVER_USER']
        self._password = config['SMTP_SERVER_PASSWORD']
        self.port = config['SMTP_SERVER_PORT']

    def send(self, recipient, body, subject=None):
        if type(body) is unicode:
            body = body.encode('utf-8')

        msg = MIMEMultipart()
        msg['To'] = '{0}'.format(recipient)
        msg['From'] = self.email_from
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        try:
            self._start()
            self._server.sendmail(self.email_from, recipient, msg.as_string())
            self._close()
        except Exception as exc:
            log.error('An error occured while trying to send email!')
            log.error(str(exc))
            raise
        else:
            log.info('Successfully sent email to {0}'.format(recipient))

    def _start(self):
        self._server = smtplib.SMTP(self.server_name)
        self._server.login(self._username, self._password)

    def _close(self):
        self._server.quit()
