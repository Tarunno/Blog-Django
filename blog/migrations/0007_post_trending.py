# Generated by Django 3.1.1 on 2020-09-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trending',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
