# Generated by Django 3.1.13 on 2021-11-16 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_master_tables.unit'),
        ),
        migrations.CreateModel(
            name='ItemAdditionalClassification',
            fields=[
                ('classification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.classification')),
                ('ref_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds_master_tables.item')),
            ],
            bases=('ocds_master_tables.classification',),
        ),
    ]