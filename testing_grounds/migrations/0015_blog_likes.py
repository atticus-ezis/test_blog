# Generated by Django 5.0.6 on 2024-06-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_grounds', '0014_alter_comment_blog_alter_comment_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
