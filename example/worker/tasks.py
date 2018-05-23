"""Defines Celery tasks."""

import logging

from worker import celery_app


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
def hello_world(task, *args, **kwargs):
    """
    Print "Hello, World!" when called.

    Parameters
    ----------
    task : :obj:`celery.Task`
        The task object itself.

    Returns
    -------
    None
        The return value doesn't matter anyway, since we have
        `task_ignore_result = True` in `config.py`.

    """
    print("Hello, World!")
