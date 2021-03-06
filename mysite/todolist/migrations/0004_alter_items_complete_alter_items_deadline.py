# Generated by Django 4.0.2 on 2022-03-10 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_items_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='deadline',
            field=models.DateTimeField(default=datetime.date(2022, 3, 10)),
        ),
    ]
