# Generated by Django 5.0.6 on 2024-06-06 02:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_grounds', '0009_alter_blog_pub_date_alter_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 6, 2, 47, 58, 134412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 6, 6, 2, 47, 58, 134752, tzinfo=datetime.timezone.utc)),
        ),
    ]
