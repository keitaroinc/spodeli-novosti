# -*-coding:utf-8-*-
import os

class BaseConfig(object):
    """Base configuration."""
    DEBUG = True
    BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@localhost:5672/')
    BROKER_POOL_LIMIT = os.getenv('BROKER_POOL_LIMIT', None)
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE', 'UTC')
    CELERYD_CONCURRENCY = os.getenv('CELERYD_CONCURRENCY', 20)
    SMTP_SERVER = os.getenv('SMTP_SERVER', None)
    SMTP_SERVER_USER = os.getenv('SMTP_SERVER_USER', None)
    SMTP_SERVER_PASSWORD = os.getenv('SMTP_SERVER_PASSWORD', None)
    SMTP_SERVER_PORT = os.getenv('SMTP_SERVER_PORT', None)
    FROM_EMAIL = os.getenv('FROM_EMAIL', 'info@keitaro.com')
    FROM_NAME = os.getenv('FROM_NAME', 'root')


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
