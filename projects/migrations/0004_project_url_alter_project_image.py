# Generated by Django 4.2.4 on 2023-10-21 11:15

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='posts/default.svg', upload_to=projects.models.user_directory_path),
        ),
    ]
