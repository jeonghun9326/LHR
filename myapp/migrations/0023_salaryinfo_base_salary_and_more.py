# Generated by Django 5.2 on 2025-05-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_salaryinfo_bank_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryinfo',
            name='base_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salaryinfo',
            name='childcare_allowance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salaryinfo',
            name='commute_allowance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salaryinfo',
            name='duty_allowance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salaryinfo',
            name='fixed_overtime_pay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salaryinfo',
            name='meal_allowance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
