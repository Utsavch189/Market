# Generated by Django 3.2.8 on 2022-06-20 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0005_alter_distributetoretailer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributetoretailer',
            name='calculation_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='distributetoretailer',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 20)),
        ),
    ]
