# Generated by Django 4.2.9 on 2024-03-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0028_alter_fin_paymentmadedetails_payment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fin_paymentmadedetails',
            name='payment_number',
            field=models.CharField(max_length=50),
        ),
    ]
