# Generated by Django 3.2.8 on 2022-06-30 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0013_auto_20220629_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributetoretailer',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 30)),
        ),
        migrations.AlterField(
            model_name='totalproducts',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 30)),
        ),
    ]