FROM python:3.10.11

# Добавляем установку пакетов с локалями
RUN apt-get update && apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Остальная часть Dockerfile (скопированный код из вашего предыдущего Dockerfile)
RUN mkdir /src
COPY pyproject.toml /src/
RUN pip install poetry
WORKDIR /src
RUN poetry config virtualenvs.create false && poetry install
COPY ./ /src/
WORKDIR /src

