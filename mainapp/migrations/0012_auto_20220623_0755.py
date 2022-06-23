# Generated by Django 3.2.8 on 2022-06-23 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_delete_deleteduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='latitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='longitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='created_at',
            field=models.DateField(verbose_name=datetime.date(2022, 6, 23)),
        ),
    ]
