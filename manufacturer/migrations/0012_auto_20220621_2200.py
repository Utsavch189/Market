# Generated by Django 3.2.8 on 2022-06-21 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0011_auto_20220620_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createdproducts',
            name='production_date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 21)),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 21)),
        ),
    ]