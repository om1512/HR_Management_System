# Generated by Django 4.1.4 on 2023-03-03 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0012_emp_task_time_taken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee_performance',
        ),
    ]