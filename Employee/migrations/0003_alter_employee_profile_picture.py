# Generated by Django 4.1.4 on 2023-02-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_rename_user_id_employee_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(upload_to='Employee/image'),
        ),
    ]