# Generated by Django 3.2.10 on 2023-02-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
