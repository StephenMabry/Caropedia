# Generated by Django 4.0.5 on 2023-04-18 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chi_api', '0004_rename_transaction_vehicletransaction'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='vehicletransaction',
            table='vehicle_transaction',
        ),
    ]