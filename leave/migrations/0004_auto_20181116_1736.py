# Generated by Django 2.1.2 on 2018-11-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20181116_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_start',
            field=models.DateField(),
        ),
    ]
