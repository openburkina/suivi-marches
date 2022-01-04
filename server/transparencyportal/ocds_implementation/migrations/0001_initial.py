# Generated by Django 3.1.13 on 2021-12-30 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ocds_contracts', '0001_initial'),
        ('ocds_master_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ocds_contracts.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=255, null=True)),
                ('implementation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ocds_implementation.implementation')),
                ('payee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payee_transactions', to='ocds_master_tables.organization')),
                ('payer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_payer_transactions', to='ocds_master_tables.organization')),
                ('value', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocds_master_tables.value')),
            ],
        ),
        migrations.CreateModel(
            name='ImplementationMilestone',
            fields=[
                ('milestone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.milestone')),
                ('ref_implementation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to='ocds_implementation.implementation')),
            ],
            bases=('ocds_master_tables.milestone',),
        ),
        migrations.CreateModel(
            name='ImplementationDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.document')),
                ('ref_implementation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='ocds_implementation.implementation')),
            ],
            bases=('ocds_master_tables.document',),
        ),
    ]
