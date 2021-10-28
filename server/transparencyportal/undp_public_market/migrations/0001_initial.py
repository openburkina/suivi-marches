# Generated by Django 3.1.13 on 2021-10-28 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessor',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('contact_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contact_website', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('budget', models.FloatField(blank=True, null=True)),
                ('operating_unit', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='master_tables.operatingunit')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='master_tables.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OfferDate',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('stage_type', models.IntegerField(default=0)),
                ('related_offer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_public_market.offer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferAgreement',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('lessor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_public_market.lessor')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_public_market.offer')),
            ],
        ),
        migrations.AddField(
            model_name='lessor',
            name='agreement',
            field=models.ManyToManyField(through='undp_public_market.OfferAgreement', to='undp_public_market.Offer'),
        ),
        migrations.CreateModel(
            name='Disbursment',
            fields=[
                ('id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('value', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('offer_agreement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='undp_public_market.offeragreement')),
            ],
        ),
    ]
