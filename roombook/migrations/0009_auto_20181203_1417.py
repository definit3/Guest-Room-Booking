# Generated by Django 2.1.2 on 2018-12-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0008_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='vacant_date',
            field=models.DateField(default='NULL', null=True),
        ),
    ]
