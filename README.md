## Как запустить проект:

 _Если у вас не установлены Docker и Docker-compose необходимо воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/)._

### Клонировать репозиторий:

```
git clone https://github.com/Maliarda/preparation_of_content_digests.git
```
```
cd preparation_of_content_digests
```

## Создать .env файл. Пример .env файла:

```
POSTGRES__URL=postgresql+asyncpg://yuor_user:your_password@localhost:5432/your_db
POSTGRES__URL_TEST=postgresql+asyncpg://your_user:your_password@localhost:5432/your_db_test

POSTGRES_DB=digestservice
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432

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

## Запуск локально
### Установка Poetry

Если у вас уже установлен Poetry, вы можете перейти к следующему разделу. 
В противном случае, следуйте инструкциям ниже, чтобы установить Poetry.

```
curl -sSL https://install.python-poetry.org | python3 -
```

Дополнительные способы установки можно найти в [Официальной документации Poetry](https://python-poetry.org/docs/)

### Установка зависимостей проекта
После установки Poetry, перейдите в каталог проекта и выполните 
следующую команду для установки зависимостей:

```
poetry install
```

Эта команда прочитает файл pyproject.toml, который содержит список зависимостей проекта, 
и создаст виртуальное окружение для проекта, в котором будут установлены все зависимости.

### Активация виртуального окружения
После успешной установки зависимостей, активируйте виртуальное окружение проекта 
с помощью команды:

```
poetry shell
```

### Управление зависимостями
Для управления зависимостями, используйте команды Poetry, такие как add, remove, update и др. 
Например:

Добавление зависимости:

```
poetry add <package-name>
```

### Создание базы
Возможно с помощью [PGAdmin](https://info-comp.ru/install-pgadmin-4-on-windows-10#nastroyka-podklyucheniya-k-postgresql) или DBeaver

### Настройка переменных окружения
1. Создать файл `.env` в корне проекта

2. Записать в этот файл следующее: 

```
POSTGRES__URL=postgresql+asyncpg://user:password@localhost:5432/digestservice
POSTGRES__URL_TEST=postgresql+asyncpg://user:password@localhost:5432/test_digestservice
SQLALCHEMY__URL=postgresql://user:password@localhost:5432/digestservice
POSTGRES_DB=тут_ваше_название_БД_какую_создали_на_предыдущем_шаге

POSTGRES_USER=тут_ваш_пользователь_БД
POSTGRES_PASSWORD=тут_ваш_пароль_от_БД
POSTGRES_HOST=localhost  
POSTGRES_PORT=5432

UVICORN__RELOAD=True
UVICORN__HOST=0.0.0.0
UVICORN__PORT=8000

PROJECT_NAME=digestservice
APP_SLUG=digestservice
API_PREFIX=/api/v1
DEBUG=True
```

### Запуск сервера

```
poetry python src/main.py
```

### Документация доступна по адресам:
[http://localhost:8000/docs](http://localhost:8000/docs)

## Заполнение базы данными

Этот файл (`data.sql`) содержит резервную копию данных для базы данных `digestservice`. 
Запустите утилиту `psql`, указав имя базы данных, куда вы хотите восстановить данные, 
и имя пользователя:

```bash
   "C:\Program Files\PostgreSQL\14\bin\psql" -d digestservice -U postgres -f path/to/data.sql
```
В контейнере это можно сделать следующим образом:

```
docker exec -it 863c903e80bc  psql -U postgres -d digestservice -f /docker-entrypoint-initdb.d/data.sql
```