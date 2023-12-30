# Generated by Django 3.1.13 on 2023-06-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_release', '0003_auto_20220103_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='ocid',
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='ocid',
            field=models.CharField(editable=False, max_length=500, unique=True),
        ),
    ]
