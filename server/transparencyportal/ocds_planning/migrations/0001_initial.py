# Generated by Django 3.1.13 on 2021-12-08 08:41

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
            name='PlanningDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('plannedProcurementNotice', 'Notice of planned procurement'), ('tenderNotice', 'Tender notice'), ('awardNotice', 'Award notice'), ('contractNotice', 'Contract notice'), ('completionCertificate', 'Completion certificate'), ('procurementPlan', 'Procurement plan'), ('biddingDocuments', 'Bidding documents'), ('technicalSpecifications', 'Technical specifications'), ('evaluationCriteria', 'Evaluation criteria'), ('evaluationReports', 'Evaluation report'), ('contractDraft', 'Contract Draft'), ('contractSigned', 'Signed contract'), ('contractArrangements', 'Arrangements for ending contract'), ('contractSchedule', 'Contract schedules'), ('physicalProgressReport', 'Physical progress reports'), ('financialProgressReport', 'Financial progress reports'), ('finalAudit', 'Final audit'), ('hearingNotice', 'Public hearing notice'), ('marketStudies', 'Market studies'), ('eligibilityCriteria', 'Eligibility criteria'), ('clarifications', 'Clarifications to bidders questions'), ('shortlistedFirms', 'Shortlisted firms'), ('environmentalImpact', 'Environmental impact'), ('assetAndLiabilityAssessment', "Assessment of government's assets and liabilities"), ('riskProvisions', 'Provisions for management of risks and liabilities'), ('winningBid', 'Winning bid'), ('complaints', 'Complaints and decisions'), ('contractAnnexe', 'Annexes to the contract'), ('contractGuarantees', 'Guarantees'), ('subContract', 'Subcontracts'), ('needsAssessment', 'Needs assessment'), ('feasibilityStudy', 'Feasibility study'), ('projectPlan', 'Project plan'), ('billOfQuantity', 'Bill of quantity'), ('bidders', 'Information on bidders'), ('conflictOfInterest', 'Conflict of interest'), ('debarments', 'Debarments'), ('illustration', 'Illustrations'), ('submissionDocuments', 'Bid submission documents'), ('contractSummary', 'Contract summary'), ('cancellationDetails', 'Cancellation details')], max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('document_format', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('planning', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ocds_planning.planning')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
