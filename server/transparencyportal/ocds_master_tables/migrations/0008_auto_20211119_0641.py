# Generated by Django 3.1.13 on 2021-11-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0007_auto_20211119_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('met', 'Met'), ('notMet', 'Not met'), ('partiallyMet', 'Partially met')], max_length=255),
        ),
    ]