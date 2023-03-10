# Generated by Django 4.1.4 on 2023-03-06 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0008_emp_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=10)),
                ('response', models.CharField(default='', max_length=100)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
