# Generated by Django 3.1.13 on 2021-11-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocds_awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awarddocument',
            name='document_type',
            field=models.CharField(choices=[('plannedProcurementNotice', 'Notice of planned procurement'), ('tenderNotice', 'Tender notice'), ('awardNotice', 'Award notice'), ('contractNotice', 'Contract notice'), ('completionCertificate', 'Completion certificate'), ('procurementPlan', 'Procurement plan'), ('biddingDocuments', 'Bidding documents'), ('technicalSpecifications', 'Technical specifications'), ('evaluationCriteria', 'Evaluation criteria'), ('evaluationReports', 'Evaluation report'), ('contractDraft', 'Contract Draft'), ('contractSigned', 'Signed contract'), ('contractArrangements', 'Arrangements for ending contract'), ('contractSchedule', 'Contract schedules'), ('physicalProgressReport', 'Physical progress reports'), ('financialProgressReport', 'Financial progress reports'), ('finalAudit', 'Final audit'), ('hearingNotice', 'Public hearing notice'), ('marketStudies', 'Market studies'), ('eligibilityCriteria', 'Eligibility criteria'), ('clarifications', 'Clarifications to bidders questions'), ('shortlistedFirms', 'Shortlisted firms'), ('environmentalImpact', 'Environmental impact'), ('assetAndLiabilityAssessment', "Assessment of government's assets and liabilities"), ('riskProvisions', 'Provisions for management of risks and liabilities'), ('winningBid', 'Winning bid'), ('complaints', 'Complaints and decisions'), ('contractAnnexe', 'Annexes to the contract'), ('contractGuarantees', 'Guarantees'), ('subContract', 'Subcontracts'), ('needsAssessment', 'Needs assessment'), ('feasibilityStudy', 'Feasibility study'), ('projectPlan', 'Project plan'), ('billOfQuantity', 'Bill of quantity'), ('bidders', 'Information on bidders'), ('conflictOfInterest', 'Conflict of interest'), ('debarments', 'Debarments'), ('illustration', 'Illustrations'), ('submissionDocuments', 'Bid submission documents'), ('contractSummary', 'Contract summary'), ('cancellationDetails', 'Cancellation details')], max_length=255),
        ),
    ]
