# Generated by Django 4.0 on 2021-12-30 00:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 30, 23, 59, 8, 568931, tzinfo=utc), help_text='Enter the date the task is due'),
        ),
    ]
