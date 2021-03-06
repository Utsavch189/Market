# Generated by Django 3.2.8 on 2022-06-03 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0002_approvedusers_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedusers',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='approvedusers',
            name='userid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
