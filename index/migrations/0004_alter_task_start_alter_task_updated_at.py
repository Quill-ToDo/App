# Generated by Django 4.0 on 2021-12-15 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, help_text='Enter the date to start working on the task', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
