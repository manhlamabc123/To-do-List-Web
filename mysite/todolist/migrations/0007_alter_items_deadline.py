# Generated by Django 4.0.2 on 2022-03-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_alter_items_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]