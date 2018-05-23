# docker-celery

A simple Python Celery application served through Docker


```
from celery import Celery

celery_app = Celery("example_app", broker="amqp://****")
celery_app.send_task("worker.tasks.hello_world", queue="test_queue")
```
