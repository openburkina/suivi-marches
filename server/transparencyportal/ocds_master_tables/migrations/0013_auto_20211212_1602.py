# Generated by Django 3.1.13 on 2021-12-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0012_auto_20211212_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='date_modified',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='due_date',
            field=models.DateField(max_length=255),
        ),
    ]
