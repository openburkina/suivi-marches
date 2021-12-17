# Generated by Django 3.1.13 on 2021-12-17 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_master_tables', '0014_auto_20211217_0503'),
        ('ocds_awards', '0006_auto_20211212_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awarddocument',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='description',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='document_format',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='id',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='language',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='title',
        ),
        migrations.RemoveField(
            model_name='awarddocument',
            name='url',
        ),
        migrations.AddField(
            model_name='awarddocument',
            name='document_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.document'),
            preserve_default=False,
        ),
    ]
