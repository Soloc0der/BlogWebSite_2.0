# Generated by Django 4.1.7 on 2023-04-07 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
