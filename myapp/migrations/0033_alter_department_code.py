# Generated by Django 5.2 on 2025-05-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_department_code_alter_department_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(default='TEMP', max_length=20),
        ),
    ]
