# Generated by Django 4.1.4 on 2023-03-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0012_employee_task_employee_feedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_task',
            name='complete_time',
            field=models.DateTimeField(default=None),
        ),
    ]