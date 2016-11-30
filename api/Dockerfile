FROM pypy:2

MAINTAINER Keitaro Inc <info@keitaro.com>

WORKDIR /srv

COPY requirements.txt /srv/

RUN pip install -r requirements.txt

COPY app /srv/app/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0", "--log-file=-", "--access-logfile=-", "app:spodelinovosti"]
