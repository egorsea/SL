# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:latest

# Python не будет пытаться создавать файлы .pyc,
ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

# чтобы пип в докере не матерился
ENV PIP_ROOT_USER_ACTION=ignore

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

RUN python3 -V
RUN apt update

# Устанавливает рабочий каталог контейнера

WORKDIR /SL

# Копирует все файлы из нашего локального проекта в контейнер
COPY . .

# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


# CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]
