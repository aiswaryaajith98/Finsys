# Generated by Django 4.2.9 on 2024-03-19 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0021_remove_fin_paymentmadedetails_debit_note_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='debit_note_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='debit_note_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='debit_note_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='debit_note_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='opening_balance_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='opening_balance_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='opening_balance_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='purchase_bill_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='purchase_bill_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='purchase_bill_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='purchase_bill_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='recurring_bill_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='recurring_bill_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='recurring_bill_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmade',
            name='recurring_bill_payment',
        ),
    ]
