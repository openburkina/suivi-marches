# Generated by Django 3.1.13 on 2022-01-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_tender', '0001_initial'),
        ('ocds_master_tables', '0001_initial'),
        ('ocds_release', '0001_initial'),
        ('ocds_awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='ocds_release.release'),
        ),
        migrations.AddField(
            model_name='award',
            name='suppliers',
            field=models.ManyToManyField(related_name='as_supplier_awards', to='ocds_master_tables.Entity'),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]