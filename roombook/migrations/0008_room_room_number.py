# Generated by Django 2.1.2 on 2018-12-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0007_auto_20181203_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.CharField(default='A00', max_length=200, null=True),
        ),
    ]