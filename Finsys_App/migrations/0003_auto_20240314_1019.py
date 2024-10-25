# Generated by Django 3.2.25 on 2024-03-14 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0002_fin_recurring_bill_items_fin_recurring_bills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
    ]