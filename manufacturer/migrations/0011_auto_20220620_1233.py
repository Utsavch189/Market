# Generated by Django 3.2.8 on 2022-06-20 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0010_auto_20220619_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createdproducts',
            name='production_date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 20)),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 20)),
        ),
    ]