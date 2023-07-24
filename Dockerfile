FROM python:3.10.11


RUN apt-get update && apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen


RUN mkdir /src
COPY pyproject.toml /src/
RUN pip install poetry
WORKDIR /src
RUN poetry config virtualenvs.create false && poetry install
COPY ./ /src/
COPY data.sql /
WORKDIR /src

CMD ["python3", "src/main.py"]

