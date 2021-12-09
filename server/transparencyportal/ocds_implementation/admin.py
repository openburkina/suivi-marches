from django.contrib import admin
from ocds_implementation.models import Implementation, ImplementationDocument, ImplementationMilestone, Transaction


class TransactionInline(admin.StackedInline):
    model = Transaction

class MilestoneInline(admin.StackedInline):
    model = ImplementationMilestone

class DocumentInline(admin.StackedInline):
    model = ImplementationDocument

@admin.register(Implementation)
class ImplementationAdmin(admin.ModelAdmin):
    inlines = [TransactionInline, MilestoneInline, DocumentInline]
