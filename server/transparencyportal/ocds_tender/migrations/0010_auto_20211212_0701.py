# Generated by Django 3.1.13 on 2021-12-12 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0011_auto_20211212_0701'),
        ('ocds_tender', '0009_auto_20211202_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tender',
            name='amendment',
        ),
        migrations.AlterField(
            model_name='tender',
            name='award_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_award_period_tenders', to='ocds_master_tables.period'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='enquiry_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_enquiry_period_tenders', to='ocds_master_tables.period'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='min_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_min_value_tenders', to='ocds_master_tables.value'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='procuring_entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_procuring_entity_tenders', to='ocds_master_tables.entity'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_tender_period_tenders', to='ocds_master_tables.period'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='as_default_value_tenders', to='ocds_master_tables.value'),
        ),
        migrations.AlterField(
            model_name='tenderdocument',
            name='date_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TenderAmendment',
            fields=[
                ('amendment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.amendment')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds_tender.tender')),
            ],
            bases=('ocds_master_tables.amendment',),
        ),
    ]