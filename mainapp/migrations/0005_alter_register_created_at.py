# Generated by Django 3.2.8 on 2022-06-06 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_register_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='created_at',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 6)),
        ),
    ]