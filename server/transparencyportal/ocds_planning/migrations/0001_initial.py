# Generated by Django 3.1.13 on 2021-12-26 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ocds_master_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raison', models.TextField(blank=True, null=True)),
                ('budget', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_master_tables.budget')),
            ],
        ),
        migrations.CreateModel(
            name='PlanningMilestone',
            fields=[
                ('milestone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.milestone')),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='milestones', to='ocds_planning.planning')),
            ],
            bases=('ocds_master_tables.milestone',),
        ),
        migrations.CreateModel(
            name='PlanningDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ocds_master_tables.document')),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='documents', to='ocds_planning.planning')),
            ],
            bases=('ocds_master_tables.document',),
        ),
    ]
