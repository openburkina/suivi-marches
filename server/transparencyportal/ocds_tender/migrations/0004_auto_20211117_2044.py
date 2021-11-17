# Generated by Django 3.1.13 on 2021-11-17 20:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0003_auto_20211117_2044'),
        ('ocds_tender', '0003_auto_20211116_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='amendment',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_master_tables.amendment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tender',
            name='number_of_tenderers',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tender',
            name='procuring_entity',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='procuring_entity', to='ocds_master_tables.entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tender',
            name='tenderer',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tenderer', to='ocds_master_tables.entity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tender',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_master_tables.entity'),
        ),
        migrations.CreateModel(
            name='TenderItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.item')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds_tender.tender')),
            ],
            bases=('ocds_master_tables.item',),
        ),
    ]