# Generated by Django 3.2.7 on 2021-09-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hierarchy',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
