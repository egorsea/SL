# Generated by Django 4.1.7 on 2023-02-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_inductive_alter_sensors_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inductive',
            options={'ordering': ('name',), 'verbose_name': 'База индуктивных датчиков', 'verbose_name_plural': 'База индуктивных датчиков'},
        ),
    ]
