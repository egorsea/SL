# Generated by Django 4.1.7 on 2023-02-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_inductive_name_alter_inductive_url_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inductive',
            name='IP',
            field=models.CharField(default='', max_length=10, null=True, verbose_name='Степень защиты'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='adjust',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Регулировка'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='connection',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Способ подключения'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='distance',
            field=models.FloatField(default='', null=True, verbose_name='Номинальное расстояние'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='flush',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Способ установки'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='housing',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Конструктивное исполнение корпуса'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='indicator',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Индикация'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='material',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Материал корпуса'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='output_structure',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Cтруктура выходного сигнала'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='output_type',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='Тип контакта'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='price',
            field=models.FloatField(default='', null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='size',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Способ подключения'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='spec',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Применение'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='stock',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Срок отгрузки'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='temperature',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Температурный диапазон'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='url_img',
            field=models.SlugField(default='', max_length=250, null=True, verbose_name='Ссылка на рисунок датчика'),
        ),
        migrations.AlterField(
            model_name='inductive',
            name='voltage',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Напряжение'),
        ),
    ]
