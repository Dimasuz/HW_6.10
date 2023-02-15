#!/bin/sh
celery -A tasks.celery_app worker -c 1
gunicorn -b 0.0.0.0:5000 app:app --capture-output
