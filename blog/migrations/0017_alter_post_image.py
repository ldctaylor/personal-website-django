# Generated by Django 4.2.4 on 2023-09-04 10:29

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.svg', upload_to=blog.models.user_directory_path),
        ),
    ]
