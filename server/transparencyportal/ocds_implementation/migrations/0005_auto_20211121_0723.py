# Generated by Django 3.1.13 on 2021-11-21 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_implementation', '0004_auto_20211119_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='implementation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocds_implementation.implementation'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='uri',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]