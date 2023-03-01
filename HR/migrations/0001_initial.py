# Generated by Django 4.1.4 on 2023-02-28 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='HR/image')),
                ('joining_date', models.DateField()),
                ('department', models.CharField(default='HR', max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('role', models.CharField(default='Management', max_length=100)),
                ('working_desk', models.CharField(max_length=50)),
                ('supervisor', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('resident_address', models.CharField(max_length=150)),
                ('hometown', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]