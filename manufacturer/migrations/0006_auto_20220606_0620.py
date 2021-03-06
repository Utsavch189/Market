# Generated by Django 3.2.8 on 2022-06-06 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0005_distribute_take_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createdproducts',
            name='author',
        ),
        migrations.AddField(
            model_name='createdproducts',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='setproduct',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='production_date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 6)),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 6)),
        ),
    ]
