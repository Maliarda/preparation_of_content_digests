## Как запустить проект:

 _Если у вас не установлены Docker и Docker-compose необходимо воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/)._

### Клонировать репозиторий и перейти в нем в папку infra в командной строке:

```
git clone https://github.com/Maliarda/preparation_of_content_digests.git
```
```
cd preparation_of_content_digests
```

## Создать .env файл. Пример .env файла:

```
POSTGRES__URL=postgresql+asyncpg://yuor_user:your_password@postgres:5432/your_db
POSTGRES__URL_TEST=postgresql+asyncpg://your_user:your_password@postgres:5432/your_db_test

UVICORN__RELOAD=True
UVICORN__HOST=127.0.0.1
UVICORN__PORT=8000

SQLALCHEMY__URL=postgresql://your_user:your_password@postgres:5432/your_db

PROJECT_NAME=digestservice
APP_SLUG=digestservice
API_PREFIX=/api/v1

DEBUG=True
```


### Собрать образ при помощи docker-compose

```
docker-compose up -d --build
```
