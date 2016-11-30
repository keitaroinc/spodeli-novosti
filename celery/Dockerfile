FROM keitaro/base:0.1

MAINTAINER Keitaro Inc <info@keitaro.com>

WORKDIR /srv

RUN apk add --no-cache python \
	    py-pip && \
    # Temporary packages to build dependencies
    apk add --no-cache --virtual .build-deps \
        gcc \
        make \
        g++ \
        alpine-sdk \
        autoconf \
        automake \
        musl-dev \
        python-dev && \
    # Remove build dependencies
    apk del .build-deps

COPY requirements.txt /srv/
COPY worker /srv/worker

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install -e /srv/worker

CMD ["celery", "worker", "--app=worker.app", "--beat", "--loglevel=DEBUG"]
