# Generated by Django 3.2.8 on 2022-06-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_alter_deleteduser_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedusers',
            name='latitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='approvedusers',
            name='longitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
