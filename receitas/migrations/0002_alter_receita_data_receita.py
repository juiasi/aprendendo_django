# Generated by Django 4.0.3 on 2022-04-08 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 4, 8, 9, 5, 56, 627969)),
        ),
    ]
