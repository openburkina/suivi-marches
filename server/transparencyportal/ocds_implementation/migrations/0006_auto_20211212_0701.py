# Generated by Django 3.1.13 on 2021-12-12 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0011_auto_20211212_0701'),
        ('ocds_contracts', '0005_auto_20211212_0701'),
        ('ocds_implementation', '0005_auto_20211121_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='provider_organization',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='receiver_organization',
        ),
        migrations.AddField(
            model_name='implementation',
            name='contract',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ocds_contracts.contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='payee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payee_transactions', to='ocds_master_tables.organization'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payer_transactions', to='ocds_master_tables.organization'),
        ),
        migrations.AlterField(
            model_name='implementationdocument',
            name='date_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
