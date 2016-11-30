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


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
