# Generated by Django 3.2.8 on 2022-06-21 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_deleteduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='deleteduser',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.date(2022, 6, 21)),
        ),
    ]