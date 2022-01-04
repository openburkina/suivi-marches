# Generated by Django 3.1.13 on 2022-01-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0001_initial'),
        ('ocds_implementation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payee_transactions', to='ocds_master_tables.entity'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payer_transactions', to='ocds_master_tables.entity'),
        ),
    ]
