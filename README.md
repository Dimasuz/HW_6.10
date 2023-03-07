Это ДЗ по celery

Для запуска приложения нужно:

1. запустить в доккере Redis
docker-compose up redis

2. запустить в доккере Mongo
docker-compose up mongo

3. запустить в терминале Celery
cd app
celery -A tasks.celery_app worker -c 1

(на этом этапе можно запустить тесты - pytest tests)

4. запустить в терминале API
python app.py

5. Далее для проверки можно запустить client

6. Также можно запустить в доккере celery и app
docker-compose up celery
docker-compose up app