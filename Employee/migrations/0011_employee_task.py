# Generated by Django 4.1.4 on 2023-03-02 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0010_rename_ending_time_employee_performance_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_time', models.DateTimeField()),
                ('complete_time', models.DateTimeField()),
                ('task', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('employee_feedback', models.CharField(default='', max_length=100)),
                ('employee_status', models.CharField(default='', max_length=20)),
                ('hr_feedback', models.CharField(default='', max_length=100)),
                ('hr_status', models.CharField(default='', max_length=20)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
