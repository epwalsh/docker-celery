"""Defines the Celery app and sets up logging."""

import logging

from celery import Celery


logging.basicConfig(level=logging.INFO)

celery_app = Celery("example_app")
celery_app.config_from_object("worker.config")
