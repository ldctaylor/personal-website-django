# Generated by Django 4.2.4 on 2023-09-01 10:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
