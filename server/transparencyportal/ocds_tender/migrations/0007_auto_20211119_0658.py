# Generated by Django 3.1.13 on 2021-11-19 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0008_auto_20211119_0641'),
        ('ocds_tender', '0006_auto_20211119_0605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tender',
            name='tenderer',
        ),
        migrations.CreateModel(
            name='Tenderer',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.entity')),
                ('ref_tender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_tender.tender')),
            ],
            bases=('ocds_master_tables.entity',),
        ),
    ]