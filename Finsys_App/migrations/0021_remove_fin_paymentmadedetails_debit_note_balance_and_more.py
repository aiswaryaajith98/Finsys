# Generated by Django 4.2.9 on 2024-03-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0020_remove_fin_paymentmadedetails_balance_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='debit_note_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='debit_note_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='debit_note_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='debit_note_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='opening_balance_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='opening_balance_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='opening_balance_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='purchase_bill_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='purchase_bill_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='purchase_bill_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='purchase_bill_payment',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='recurring_bill_balance',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='recurring_bill_date',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='recurring_bill_number',
        ),
        migrations.RemoveField(
            model_name='fin_paymentmadedetails',
            name='recurring_bill_payment',
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='debit_note_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='debit_note_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='debit_note_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='debit_note_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='opening_balance_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='opening_balance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='opening_balance_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='purchase_bill_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='purchase_bill_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='purchase_bill_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='purchase_bill_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='recurring_bill_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='recurring_bill_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='recurring_bill_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmade',
            name='recurring_bill_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmadedetails',
            name='balance_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmadedetails',
            name='bill_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmadedetails',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='fin_paymentmadedetails',
            name='payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fin_paymentmadedetails',
            name='type',
            field=models.CharField(choices=[('Opening Balance', 'Opening Balance'), ('Recurring Bill', 'Recurring Bill'), ('Purchase Bill', 'Purchase Bill'), ('Debit Note', 'Debit Note')], max_length=100, null=True),
        ),
    ]