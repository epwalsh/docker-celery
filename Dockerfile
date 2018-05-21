FROM python:3.5-alpine

# Install system packages
RUN apk add --update \
        supervisor && \
    rm -rf /var/cache/apk/*

WORKDIR /opt/python/app/

# Install python dependencies.
RUN pip install celery

# Copy supervisord configuration.
COPY supervisord.conf /etc/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
