# Generated by Django 3.1.13 on 2021-09-20 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('undp_outputs', '0001_initial'),
        ('master_tables', '0001_initial'),
        ('undp_projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('classification_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(db_index=True, max_length=100)),
                ('vendor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(db_index=True)),
                ('ref', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('line_nbr', models.FloatField(blank=True, null=True)),
                ('partner', models.CharField(blank=True, max_length=15, null=True)),
                ('business_unit', models.CharField(blank=True, max_length=15, null=True)),
                ('operating_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='master_tables.operatingunit')),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_outputs.output')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_projects.project')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_purchase_orders.vendor')),
            ],
        ),
    ]
