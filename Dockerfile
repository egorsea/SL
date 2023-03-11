# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.10.10

# Python не будет пытаться создавать файлы .pyc,
ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1


# Устанавливает рабочий каталог контейнера

WORKDIR /SL

# Копирует все файлы из нашего локального проекта в контейнер
COPY . .

RUN pip install --upgrade pip
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# CMD ["gunicorn","-b","0.0.0.0:8001","soaqaz.wsgi:application"]
