# Generated by Django 4.1.4 on 2023-03-02 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0013_alter_employee_task_complete_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_task',
            name='complete_time',
        ),
    ]
