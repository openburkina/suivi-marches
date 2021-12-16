# Generated by Django 3.1.13 on 2021-12-16 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0013_auto_20211212_1602'),
        ('ocds_release', '0012_auto_20211216_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='implementation_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ocds_master_tables.address'),
        ),
    ]
