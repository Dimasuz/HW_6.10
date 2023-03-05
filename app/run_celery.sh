#!/bin/sh
celery -A tasks.celery_app worker -c 1