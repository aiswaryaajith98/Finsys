# Generated by Django 4.2.9 on 2024-03-16 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0009_fin_paymentmade_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_paymentmade',
            name='total_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 16)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 16)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 16)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 16)),
        ),
    ]
