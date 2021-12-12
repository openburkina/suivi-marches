# Generated by Django 3.1.13 on 2021-12-12 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_tender', '0011_auto_20211212_1504'),
        ('ocds_planning', '0006_auto_20211212_1504'),
        ('ocds_release', '0010_auto_20211212_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedrelease',
            name='ref_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='releases', to='ocds_release.record'),
        ),
        migrations.AlterField(
            model_name='release',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='releases', to='ocds_tender.buyer'),
        ),
        migrations.AlterField(
            model_name='release',
            name='planning',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_planning.planning'),
        ),
        migrations.AlterField(
            model_name='release',
            name='tender',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_tender.tender'),
        ),
    ]
