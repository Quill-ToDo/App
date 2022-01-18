# Generated by Django 4.0 on 2021-12-26 01:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 23, 59, 52, 871508, tzinfo=utc), help_text='Enter the date the task is due'),
        ),
    ]