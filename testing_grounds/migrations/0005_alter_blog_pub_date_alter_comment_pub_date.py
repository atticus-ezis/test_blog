# Generated by Django 5.0.6 on 2024-06-05 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_grounds', '0004_alter_blog_pub_date_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 5, 8, 7, 11, 822829)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 5, 15, 7, 11, 822975, tzinfo=datetime.timezone.utc)),
        ),
    ]
