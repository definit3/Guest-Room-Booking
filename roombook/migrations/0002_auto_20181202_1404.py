# Generated by Django 2.1.2 on 2018-12-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='alloted',
        ),
        migrations.AlterField(
            model_name='room',
            name='vacant',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
