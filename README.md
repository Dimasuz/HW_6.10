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

Далее для проверки можно запустить client.py

Все работает.

Но если собрать для celery и API доккеры, 
то получаем какую-то ошибку соединения с Mongo:
"""
pymongo.errors.ServerSelectionTimeoutError: 127.0.0.1:27017: 
[Errno 111] Connection refused, Timeout: 30s, Topology Description: 
<TopologyDescription id: 640488e6ca009bc201e07816, topology_type: 
Unknown, servers: [<ServerDescription ('127.0.0.1', 27017) 
server_type: Unknown, rtt: None, error=AutoReconnect('127.0.0.1:27017: 
[Errno 111] Connection refused')>]>
"""
Перепробавона множество вариантов настройти flask с mongo,
ничего не помогло.
Мало того, попробовал загрузить проект со ссылки на лекции, получил туже ошибку.


docker-compose up celery
