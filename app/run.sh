#!/bin/sh
celery -A tasks.celery_app worker -l info -P gevent
gunicorn -b 0.0.0.0:5000 app:app --capture-output
