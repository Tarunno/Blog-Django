# Generated by Django 3.1.1 on 2021-06-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200913_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.BooleanField(default=False),
        ),
    ]
