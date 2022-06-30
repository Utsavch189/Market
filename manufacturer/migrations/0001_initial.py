# Generated by Django 3.2.8 on 2022-06-05 08:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SetProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreatedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('production_no', models.CharField(blank=True, max_length=150, null=True)),
                ('production_date', models.DateField(verbose_name=datetime.date(2022, 6, 5))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manufacturer.setproduct')),
            ],
        ),
    ]
