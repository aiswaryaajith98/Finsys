# Generated by Django 4.2.9 on 2024-03-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0010_fin_paymentmade_total_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_paymentmade',
            name='balance_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='bill_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
