# Generated by Django 3.2.7 on 2021-09-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_remove_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(null=True),
        ),
    ]