# Generated by Django 3.1.13 on 2021-12-12 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_planning', '0005_auto_20211212_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planningdocument',
            name='planning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='documents', to='ocds_planning.planning'),
        ),
        migrations.AlterField(
            model_name='planningmilestone',
            name='planning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='milestones', to='ocds_planning.planning'),
        ),
    ]