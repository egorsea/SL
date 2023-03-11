from django.db import models

# Create your models here.

class Sensors(models.Model):
    category_name = models.CharField('Категория', max_length=50, default='')
    sensor_type = models.CharField('Тип датчика', max_length=50, default='')
    sensor_symbol = models.CharField('Обозначение', max_length=50, default='')
    sensor_url = models.SlugField('Ссылка на сайт производителя', max_length=250, unique=True, default='')
    sensor_price = models.CharField('Цена', max_length=50, default='')
    sensor_in_stock = models.CharField('Наличие', max_length=50, default='')

    # def __str__(self) -> str:
        # return f'{self.sensor_type} {self.sensor_symbol}'

    class Meta:
        verbose_name = 'Перечень датчиков'
        verbose_name_plural = 'Перечень датчиков'
        ordering = ('sensor_symbol',)


class Inductive(models.Model):
    category = models.CharField('Категория датчика', max_length=30, default='')
    type = models.CharField('Тип датчика', max_length=30, default='')
    name = models.CharField('Обозначение датчика', max_length=20, default='', unique=True)
    url = models.SlugField('Ссылка на сайт производителя', max_length=250, unique=True, default='')
    url_img = models.SlugField('Ссылка на рисунок датчика', max_length=250, default='', null=True)
    price = models.FloatField('Цена', default='', null=True)
    stock = models.CharField('Срок отгрузки', max_length=50, default='', null=True)
    manufacturer = models.CharField('Производитель', max_length=20, default='')
    flush = models.CharField('Способ установки', max_length=20, default='', null=True)
    spec = models.CharField('Применение', max_length=50, default='', null=True)
    housing = models.CharField('Конструктивное исполнение корпуса', max_length=50, default='', null=True)
    connection = models.CharField('Способ подключения', max_length=50, default='', null=True)
    size = models.CharField('Габарит датчика', max_length=30, default='', null=True)
    material = models.CharField('Материал корпуса', max_length=20, default='', null=True)
    IP =  models.CharField('Степень защиты', max_length=10, default='', null=True)
    output_structure = models.CharField('Cтруктура выходного сигнала', max_length=40, default='', null=True)
    voltage = models.CharField('Напряжение', max_length=30, default='', null=True)
    output_type = models.CharField('Функция выхода', max_length=20, default='', null=True)
    adjust = models.CharField('Регулировка', max_length=20, default='', null=True)
    distance = models.FloatField('Номинальное расстояние', default='', null=True)
    indicator = models.CharField('Индикация', max_length=20, default='', null=True)
    temperature = models.CharField('Температурный диапазон', max_length=30, default='', null=True)


    class Meta:
        verbose_name = 'База индуктивных датчиков'
        verbose_name_plural = 'База индуктивных датчиков'
        # ordering = ('name',)
