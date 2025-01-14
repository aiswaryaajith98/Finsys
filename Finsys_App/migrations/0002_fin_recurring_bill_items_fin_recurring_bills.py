# Generated by Django 3.2.25 on 2024-03-13 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Recurring_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurring_bill_number', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_number', models.IntegerField(blank=True, null=True)),
                ('bill_number', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('expected_shipment_date', models.DateField(blank=True, null=True)),
                ('purchase_order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='document')),
                ('sub_total', models.FloatField(blank=True, null=True)),
                ('cgst', models.FloatField(blank=True, null=True)),
                ('sgst', models.FloatField(blank=True, null=True)),
                ('taxAmount_igst', models.FloatField(blank=True, null=True)),
                ('shipping_charge', models.FloatField(blank=True, null=True)),
                ('adjustment', models.FloatField(blank=True, null=True)),
                ('grand_total', models.FloatField(blank=True, null=True)),
                ('advanceAmount_paid', models.FloatField(blank=True, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='recurring_bill_attachments')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('company_payment_terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_payment_terms')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
                ('repeat_every', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_companyrepeatevery')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Recurring_Bill_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('tax_rate', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_items')),
                ('recurring_bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_recurring_bills')),
            ],
        ),
    ]
