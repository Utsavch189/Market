# Generated by Django 3.2.8 on 2022-06-26 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_auto_20220623_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleteduser',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2022, 6, 26)),
        ),
    ]