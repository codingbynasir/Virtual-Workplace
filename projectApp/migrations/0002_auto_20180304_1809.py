# Generated by Django 2.0 on 2018-03-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='started_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
