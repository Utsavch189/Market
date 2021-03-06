# Generated by Django 3.2.8 on 2022-06-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_delete_setproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=500, null=True)),
                ('whatsapp_no', models.CharField(blank=True, max_length=500, null=True)),
                ('role', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
