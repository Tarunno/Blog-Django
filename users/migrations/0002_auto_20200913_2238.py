# Generated by Django 3.1.1 on 2020-09-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]
