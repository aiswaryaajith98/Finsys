# Generated by Django 4.2.9 on 2024-03-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0016_alter_fin_paymentmadedetails_balance_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fin_paymentmadedetails',
            name='bill_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
