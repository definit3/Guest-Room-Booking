# Generated by Django 2.1.2 on 2018-12-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0003_auto_20181202_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='approve',
            field=models.BooleanField(default=False, null=True),
        ),
    ]