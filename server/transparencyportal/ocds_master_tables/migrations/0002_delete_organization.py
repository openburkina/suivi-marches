# Generated by Django 3.1.13 on 2022-01-02 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_implementation', '0002_auto_20220102_1459'),
        ('ocds_master_tables', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
