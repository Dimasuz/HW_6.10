import os

# CELERY_BROKER = os.getenv("CELERY_BROKER")
# CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
# MONGO_DSN = os.getenv("MONGO_DSN")

CELERY_BROKER = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
MONGO_DSN = "mongodb://app:123@127.0.0.1:27017/files?authSource=admin"

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
