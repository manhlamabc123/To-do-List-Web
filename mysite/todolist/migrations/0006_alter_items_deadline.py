# Generated by Django 4.0.2 on 2022-03-10 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_items_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 14, 6, 31, 325899, tzinfo=utc)),
        ),
    ]
