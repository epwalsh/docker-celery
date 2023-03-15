# docker-celery

This is a Docker image for Python Celery workers.

## Details

- Built on Alpine Linux for a super small image size.
- The Celery process is managed by Supervisor, and is pointed to the application
through an environment variable.
- Other environment variables control the queue name, number of workers, and
log level.
- Uses an external broker so the number of workers can be scaled up by simply scaling the number of containers.

## Quick start example

This will show you how to get the
[example application](https://github.com/epwalsh/docker-celery/tree/master/example)
running.

In order to get started, you will need a message broker running, such as RabbitMQ.
If you don't already have one, you can get a free RabbitMQ instance for development
purposes through [CloudAMQP](https://customer.cloudamqp.com/instance/create?plan=lemur).
It should only take a few minutes to set up.

Once you have one, take note of the AMQP URL, which will look something like this:
`amqp://****:*****@donkey.rmqp.cloudamqp.com/****`.

Now, if you haven't already, clone this repository and pull the Docker image:

```
git clone https://github.com/epwalsh/docker-celery && cd docker-celery
docker pull epwalsh/docker-celery
```

Next, `cd` into the `example/` directory and create the environment file `access.txt`
with the AMQP URL:

```
cd example
cp access.sample.txt access.txt
```

Edit the first line in `access.txt` so that `BROKER_URL` is set to your AMQP URL.
Now build and run the image with

```
docker build -t YOUR-NAME/celery-test .
docker run --env-file=./access.txt --rm YOUR-NAME/celery-test
```

If everything works, the Celery worker should start and produce some messages
like this:

```
[2018-05-26 21:33:29,024: INFO/MainProcess] Connected to amqp://****:**@donkey.rmq.cloudamqp.com:****/****
[2018-05-26 21:33:29,582: INFO/MainProcess] mingle: searching for neighbors
[2018-05-26 21:33:31,737: INFO/MainProcess] mingle: all alone
[2018-05-26 21:33:32,877: INFO/MainProcess] test_queue-worker@4e39494c2213 ready.
```

You can now send a task to your worker with a Python script like this:

```
from celery import Celery

celery_app = Celery("example_app", broker="amqp://****")  # `broker` should be your BROKER_URL from access.txt
celery_app.send_task("worker.tasks.hello_world", queue="test_queue")
```
