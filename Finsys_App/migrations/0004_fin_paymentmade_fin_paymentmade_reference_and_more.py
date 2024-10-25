# Generated by Django 4.2.9 on 2024-03-14 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0003_auto_20240314_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_PaymentMade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.BigIntegerField()),
                ('payment_number', models.CharField(max_length=50)),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(max_length=50)),
                ('cheque_number', models.CharField(blank=True, max_length=50, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_account', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Save', 'Save')], max_length=10)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_PaymentMade_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.BigIntegerField()),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_PaymentMade_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(blank=True, choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=20, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('paymentmade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_paymentmade')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_PaymentMade_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('paymentmade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_paymentmade')),
            ],
        ),
    ]