# Generated by Django 3.2.7 on 2021-11-29 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_cvrole_cvroleitem_roledescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvroleitem',
            name='cv_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roleitems', to='portfolio.cvrole'),
        ),
    ]
