# Generated by Django 4.0.6 on 2022-07-26 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_number', models.CharField(blank=True, max_length=200, null=True)),
                ('lit_dates', models.CharField(blank=True, max_length=200, null=True)),
                ('claimant', models.CharField(blank=True, max_length=100, null=True)),
                ('action_required', models.CharField(blank=True, max_length=200, null=True)),
                ('in_suit', models.CharField(blank=True, max_length=100, null=True)),
                ('dc_assigned', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('date_coverage_letter_sent', models.CharField(blank=True, max_length=100, null=True)),
                ('days_since_last_note', models.CharField(blank=True, max_length=100, null=True)),
                ('insured_facility', models.CharField(blank=True, max_length=200, null=True)),
                ('coverage_letter', models.CharField(blank=True, max_length=200, null=True)),
                ('settlement_value', models.CharField(blank=True, max_length=200, null=True)),
                ('insurer_policy', models.CharField(blank=True, max_length=200, null=True)),
                ('bulk_insured', models.CharField(blank=True, max_length=200, null=True)),
                ('claim_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimNum', models.CharField(blank=True, max_length=200, null=True)),
                ('emailSubject', models.CharField(blank=True, max_length=200, null=True)),
                ('emailFrom', models.CharField(blank=True, max_length=200, null=True)),
                ('emailFromAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('emailTo', models.CharField(blank=True, max_length=200, null=True)),
                ('emailBody', models.CharField(blank=True, max_length=10000, null=True)),
                ('claim', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='capstone2_app.claim')),
            ],
        ),
    ]
