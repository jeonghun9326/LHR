# Generated by Django 5.2 on 2025-05-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_employee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='연락처'),
        ),
    ]
